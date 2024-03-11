# This script is used to print the posts in a csv format

from colorama import Fore

def print_post(posts):
    print("handle, timestamp, likes, reposts, replies, text")
    for post in posts.feed:
        replaced_post_text = post.post.record.text.replace("\n", f"{Fore.YELLOW}\\n{Fore.RESET}")
        print(f"{post.post.author.handle},{post.post.record.created_at},{post.post.like_count},{post.post.repost_count},{post.post.reply_count},{replaced_post_text}")