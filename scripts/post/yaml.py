# This script is used to print the posts in a yaml format

from colorama import Fore
import configparser

config = configparser.ConfigParser()
config.read(f'scripts/post/config/{__name__}.ini')

cfg = config.getint('config', 'cfg')
reverse = config.getboolean('config', 'reverse')

def print_post(posts):
    feed = posts.feed
    if reverse:
        feed = reversed(feed)

    print(f"posts:")
    for post in feed:
        replaced_post_text = post.post.record.text.replace("\n", f"{Fore.YELLOW}\\n{Fore.RESET}")
        print(f"  - id: {post.post.uri}")
        print(f"    handle: {post.post.author.handle}")
        print(f"    timestamp: {post.post.record.created_at}")
        print(f"    likes: {post.post.like_count}")
        print(f"    reposts: {post.post.repost_count}")
        print(f"    replies: {post.post.reply_count}")
        print(f"    text: {replaced_post_text}")
        print(f"")