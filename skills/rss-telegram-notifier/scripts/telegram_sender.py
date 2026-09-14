#!/usr/bin/env python3
"""
Telegram Sender - 发送格式化的 RSS 文章到 Telegram
"""

import json
import sys
import os

def format_article(article):
    """格式化单篇文章为美观的 Telegram 消息"""
    title = article.get('title', '无标题')
    link = article.get('link', '')
    summary = article.get('summary', '')
    source = article.get('source', '未知来源')
    published = article.get('published', '')
    
    # 清理摘要中的 HTML 标签
    import re
    summary = re.sub(r'<[^>]+>', '', summary)
    if len(summary) > 280:
        summary = summary[:277] + "..."
    
    # 构建美观的消息格式
    message = f"""📰 <b>{title}</b>

{summary}

📎 <a href=\"{link}\">阅读原文</a>
📌 {source}"""
    
    if published:
        message += f"\n🕐 {published}"
    
    return message

def format_digest(articles):
    """格式化多篇为摘要形式"""
    if len(articles) == 1:
        return format_article(articles[0])
    
    message = f"📬 <b>今日更新 ({len(articles)} 篇)</b>\n\n"
    
    for i, article in enumerate(articles, 1):
        title = article.get('title', '无标题')
        link = article.get('link', '')
        source = article.get('source', '未知来源')
        
        message += f"{i}. <b>{title}</b>\n"
        message += f"   <a href=\"{link}\">阅读原文</a> | 📌 {source}\n\n"
    
    return message.strip()

def send_to_telegram(bot_token, chat_id, message, silent=False):
    """发送消息到 Telegram"""
    import urllib.request
    import urllib.parse
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML',
        'disable_web_page_preview': False,
        'disable_notification': silent
    }
    
    data = urllib.parse.urlencode(payload).encode('utf-8')
    
    try:
        req = urllib.request.Request(url, data=data, method='POST')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result.get('ok', False)
    except Exception as e:
        print(f"Error sending to Telegram: {e}", file=sys.stderr)
        return False

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python telegram_sender.py <bot_token> <chat_id> '<articles_json>'")
        print("       or echo '[{article}]' | python telegram_sender.py <bot_token> <chat_id> -")
        sys.exit(1)
    
    bot_token = sys.argv[1]
    chat_id = sys.argv[2]
    articles_input = sys.argv[3]
    
    # 从参数或stdin读取
    if articles_input == '-':
        articles_input = sys.stdin.read()
    
    try:
        articles = json.loads(articles_input)
        if not isinstance(articles, list):
            articles = [articles]
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)
    
    if not articles:
        print("No articles to send")
        sys.exit(0)
    
    # 根据数量决定发送方式
    if len(articles) <= 3:
        # 少量文章，逐条发送
        for article in articles:
            message = format_article(article)
            success = send_to_telegram(bot_token, chat_id, message)
            if not success:
                sys.exit(1)
    else:
        # 多篇文章，发送摘要
        message = format_digest(articles)
        success = send_to_telegram(bot_token, chat_id, message)
        if not success:
            sys.exit(1)
    
    print(f"Successfully sent {len(articles)} article(s)")
