# This script is used to print the posts in a csv format

from colorama import Fore
import configparser

config = configparser.ConfigParser()
config.read(f'scripts/post/config/csv.ini')

reverse = config.getboolean('config', 'reverse')

def print_post(posts):
    feed = posts.feed
    if reverse:
        feed = reversed(feed)

    print("handle, timestamp, likes, reposts, replies, text")
    for post in feed:
        replaced_post_text = post.post.record.text.replace("\n", f"{Fore.YELLOW}\\n{Fore.RESET}")
        print(f"{post.post.author.handle},{post.post.record.created_at},{post.post.like_count},{post.post.repost_count},{post.post.reply_count},{replaced_post_text}")