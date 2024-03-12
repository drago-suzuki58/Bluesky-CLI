# This script is used to print the posts in a xml format

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

    print("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
    for post in feed:
        replaced_post_text = post.post.record.text.replace("\n", f"{Fore.YELLOW}\\n{Fore.RESET}")
        print(f"<post>")
        print(f"    <handle>{post.post.author.handle}</handle>")
        print(f"    <timestamp>{post.post.record.created_at}</timestamp>")
        print(f"    <likes>{post.post.like_count}</likes>")
        print(f"    <reposts>{post.post.repost_count}</reposts>")
        print(f"    <replies>{post.post.reply_count}</replies>")
        print(f"    <text>{replaced_post_text}</text>")
        print(f"</post>")