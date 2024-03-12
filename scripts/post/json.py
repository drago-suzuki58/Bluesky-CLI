# This script is used to print the posts in a json format

import configparser
import json
from colorama import Fore

# Load configuration once
config = configparser.ConfigParser()
config.read(f'scripts/post/config/json.ini')

indent = config.getint('config', 'indent')
reverse = config.getboolean('config', 'reverse')

def print_post(posts):
    feed = posts.feed
    if reverse:
        feed = reversed(feed)

    posts_json = []
    for post in feed:
        replaced_post_text = post.post.record.text.replace("\n", f"{Fore.YELLOW}\\n{Fore.RESET}")
        post_dict = {
            "handle": post.post.author.handle,
            "timestamp": str(post.post.record.created_at),
            "likes": post.post.like_count,
            "reposts": post.post.repost_count,
            "replies": post.post.reply_count,
            "text": replaced_post_text,
        }
        posts_json.append(post_dict)

    print(json.dumps({"posts": posts_json}, indent=indent, ensure_ascii=False))