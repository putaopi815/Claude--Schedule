#!/usr/bin/env python3
"""
钉钉群机器人推送脚本
用于将每日 AI+UX Digest 推送到钉钉群

使用方式:
    python3 dingtalk_notify.py                          # 推送今天的日报
    python3 dingtalk_notify.py 2026-04-10               # 推送指定日期的日报
    python3 dingtalk_notify.py --file path/to/file.md   # 推送指定文件
    python3 dingtalk_notify.py --text "自定义消息"       # 推送自定义文本
"""

import hashlib
import hmac
import base64
import time
import urllib.parse
import json
import sys
import os
import re
from datetime import date
from pathlib import Path

import requests


def load_env(env_path=None):
    """从 .env 文件加载环境变量"""
    if env_path is None:
        env_path = Path(__file__).parent / ".env"
    if not env_path.exists():
        return
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip()
            if key and value:
                os.environ.setdefault(key, value)


def get_signed_url(webhook_url, secret):
    """生成带签名的钉钉 webhook URL (HMAC-SHA256)"""
    timestamp = str(round(time.time() * 1000))
    string_to_sign = f"{timestamp}\n{secret}"
    hmac_code = hmac.new(
        secret.encode("utf-8"),
        string_to_sign.encode("utf-8"),
        digestmod=hashlib.sha256,
    ).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return f"{webhook_url}&timestamp={timestamp}&sign={sign}"


def truncate_for_dingtalk(text, max_length=18000):
    """钉钉消息有长度限制，截断过长内容"""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "\n\n---\n*（内容过长，已截断。完整内容请查看 GitHub 仓库）*"


def md_to_dingtalk_markdown(content):
    """将标准 Markdown 适配为钉钉支持的 Markdown 子集"""
    # 钉钉 Markdown 支持: 标题、加粗、链接、图片、有序/无序列表、引用
    # 不支持: 表格、代码块高亮、删除线等
    # 移除 HTML 标签
    content = re.sub(r"<[^>]+>", "", content)
    return content


def extract_title(content):
    """从 Markdown 内容中提取标题"""
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            return line.lstrip("# ").strip()
    return "AI + UX Daily Digest"


def send_markdown(title, content, webhook_url, secret):
    """发送 Markdown 消息到钉钉群"""
    url = get_signed_url(webhook_url, secret)
    adapted_content = md_to_dingtalk_markdown(content)
    adapted_content = truncate_for_dingtalk(adapted_content)

    payload = {
        "msgtype": "markdown",
        "markdown": {
            "title": title,
            "text": adapted_content,
        },
    }

    headers = {"Content-Type": "application/json; charset=utf-8"}
    resp = requests.post(url, json=payload, headers=headers, timeout=10)
    result = resp.json()

    if result.get("errcode") == 0:
        print(f"✅ 推送成功: {title}")
        return True
    else:
        print(f"❌ 推送失败: {result}")
        return False


def send_text(content, webhook_url, secret):
    """发送纯文本消息到钉钉群"""
    url = get_signed_url(webhook_url, secret)

    payload = {
        "msgtype": "text",
        "text": {
            "content": content,
        },
    }

    headers = {"Content-Type": "application/json; charset=utf-8"}
    resp = requests.post(url, json=payload, headers=headers, timeout=10)
    result = resp.json()

    if result.get("errcode") == 0:
        print(f"✅ 推送成功")
        return True
    else:
        print(f"❌ 推送失败: {result}")
        return False


def find_digest_file(target_date=None):
    """查找日报文件"""
    project_dir = Path(__file__).parent
    if target_date is None:
        target_date = date.today().isoformat()
    filename = f"{target_date}-ai-ux-daily.md"
    filepath = project_dir / filename
    if filepath.exists():
        return filepath
    # 尝试查找最新的日报文件
    md_files = sorted(project_dir.glob("*-ai-ux-daily.md"), reverse=True)
    if md_files:
        print(f"⚠️  未找到 {filename}，使用最新日报: {md_files[0].name}")
        return md_files[0]
    return None


def main():
    load_env()

    webhook_url = os.environ.get("DINGTALK_WEBHOOK")
    secret = os.environ.get("DINGTALK_SECRET")

    if not webhook_url or not secret:
        print("❌ 缺少钉钉配置。请设置环境变量 DINGTALK_WEBHOOK 和 DINGTALK_SECRET")
        print("   或在 .env 文件中配置")
        sys.exit(1)

    args = sys.argv[1:]

    # --text 模式: 发送自定义文本
    if "--text" in args:
        idx = args.index("--text")
        if idx + 1 < len(args):
            text = args[idx + 1]
            send_text(text, webhook_url, secret)
            return
        else:
            print("❌ --text 后需要提供消息内容")
            sys.exit(1)

    # --file 模式: 推送指定文件
    if "--file" in args:
        idx = args.index("--file")
        if idx + 1 < len(args):
            filepath = Path(args[idx + 1])
            if not filepath.exists():
                print(f"❌ 文件不存在: {filepath}")
                sys.exit(1)
            content = filepath.read_text(encoding="utf-8")
            title = extract_title(content)
            send_markdown(title, content, webhook_url, secret)
            return
        else:
            print("❌ --file 后需要提供文件路径")
            sys.exit(1)

    # 日期模式或默认模式
    target_date = args[0] if args else None
    filepath = find_digest_file(target_date)

    if filepath is None:
        print("❌ 未找到日报文件")
        sys.exit(1)

    content = filepath.read_text(encoding="utf-8")
    title = extract_title(content)
    print(f"📤 正在推送: {filepath.name}")
    send_markdown(title, content, webhook_url, secret)


if __name__ == "__main__":
    main()
