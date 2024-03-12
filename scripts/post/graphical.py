# This script is used to print the posts in a graphical format

import configparser
import textwrap
import os

config = configparser.ConfigParser()
config.read(f'scripts/post/config/graphical.ini')

scale_factor = config.getint('config', 'scale_factor')
limit = config.getint('config', 'limit')
reverse = config.getboolean('config', 'reverse')

def scale_and_limit(value):
    scaled_value = value / scale_factor
    if scaled_value > limit:
        return '█' * limit + '+'
    else:
        return '█' * int(scaled_value)

def log_and_print(message, file):
    print(message)
    file.write(message + "\n")

def print_post(posts):
    feed = posts.feed
    if reverse:
        feed = reversed(feed)

    if not os.path.exists('log'):
        os.makedirs('log')

    for post in feed:
        content_lines = textwrap.wrap(post.post.record.text, width=60)

        with open('log/get_post_graphical.log', 'a' ,encoding="utf-8") as f:
            log_and_print("------------------------------------------------------------------------------------", f)
            log_and_print(f"Post ID:   {post.post.uri}", f)
            log_and_print(f"Timestamp: {post.post.record.created_at}", f)
            log_and_print(f"Username:  {post.post.author.handle}", f)
            log_and_print("------------------------------------------------------------------------------------", f)
            log_and_print(f"Content:", f)
            for line in content_lines:
                log_and_print(f"{line}", f)
            log_and_print("------------------------------------------------------------------------------------", f)
            log_and_print(f"Likes  :   {scale_and_limit(post.post.like_count):<70}{post.post.like_count}", f)
            log_and_print(f"Reposts:   {scale_and_limit(post.post.repost_count):<70}{post.post.repost_count}", f)
            log_and_print(f"Replies:   {scale_and_limit(post.post.reply_count):<70}{post.post.reply_count}", f)
            log_and_print("------------------------------------------------------------------------------------", f)
            log_and_print("", f)