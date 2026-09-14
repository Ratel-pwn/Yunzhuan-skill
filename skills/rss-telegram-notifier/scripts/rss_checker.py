#!/usr/bin/env python3
"""
RSS Checker - 检查 RSS 源并返回新文章 (纯标准库实现)
"""

import json
import hashlib
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

def get_article_id(article):
    """生成文章唯一ID"""
    id_str = article.get('link', '') or article.get('title', '')
    return hashlib.md5(id_str.encode()).hexdigest()

def load_seen_articles(state_file):
    """加载已发送过的文章ID"""
    if Path(state_file).exists():
        with open(state_file, 'r', encoding='utf-8') as f:
            return set(json.load(f))
    return set()

def save_seen_articles(state_file, seen_ids):
    """保存已发送过的文章ID"""
    Path(state_file).parent.mkdir(parents=True, exist_ok=True)
    with open(state_file, 'w', encoding='utf-8') as f:
        json.dump(list(seen_ids), f, ensure_ascii=False, indent=2)

def fetch_rss(url):
    """获取 RSS 内容"""
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (compatible; RSS Bot/1.0)'
        })
        with urllib.request.urlopen(req, timeout=30) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=__import__('sys').stderr)
        return None

def parse_feed(url, max_entries=5):
    """解析 RSS 源"""
    content = fetch_rss(url)
    if not content:
        return []
    
    try:
        root = ET.fromstring(content)
        
        # 确定 RSS 或 Atom 格式
        if root.tag == 'rss' or root.tag.endswith('rss'):
            channel = root.find('channel')
            if channel is None:
                return []
            items = channel.findall('item')[:max_entries]
            source_title = channel.findtext('title', url)
        elif root.tag.endswith('feed'):  # Atom
            items = root.findall('.//{http://www.w3.org/2005/Atom}entry')[:max_entries]
            if not items:
                items = root.findall('entry')[:max_entries]
            source_title = root.findtext('{http://www.w3.org/2005/Atom}title', url)
            if not source_title:
                source_title = root.findtext('title', url)
        else:
            return []
        
        articles = []
        for item in items:
            # 尝试不同的标签名（RSS vs Atom）
            title = item.findtext('title', '')
            link_elem = item.find('link')
            if link_elem is not None:
                link = link_elem.get('href', '') or link_elem.text or ''
            else:
                link = item.findtext('link', '')
            
            summary = item.findtext('description', '') or item.findtext('summary', '')
            published = item.findtext('pubDate', '') or item.findtext('published', '')
            
            articles.append({
                'id': get_article_id({'title': title, 'link': link}),
                'title': title or '无标题',
                'link': link or url,
                'summary': summary[:500] if summary else '',
                'published': published,
                'source': source_title
            })
        
        return articles
    except Exception as e:
        print(f"Error parsing {url}: {e}", file=__import__('sys').stderr)
        return []

def check_feeds(config_file, state_file):
    """检查所有 RSS 源，返回新文章"""
    with open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    seen_ids = load_seen_articles(state_file)
    all_new_articles = []
    
    for feed_config in config.get('feeds', []):
        url = feed_config.get('url')
        max_entries = feed_config.get('max_entries', 5)
        
        articles = parse_feed(url, max_entries)
        
        for article in articles:
            if article['id'] not in seen_ids:
                all_new_articles.append(article)
                seen_ids.add(article['id'])
    
    # 保存更新后的状态
    save_seen_articles(state_file, seen_ids)
    
    return all_new_articles

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python rss_checker.py <config.json> <state.json>")
        print("Output: JSON array of new articles to stdout")
        sys.exit(1)
    
    config_file = sys.argv[1]
    state_file = sys.argv[2]
    
    new_articles = check_feeds(config_file, state_file)
    print(json.dumps(new_articles, ensure_ascii=False, indent=2))
