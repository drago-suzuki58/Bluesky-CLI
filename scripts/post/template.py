# This script is temleted to be used as a template for new post scripts.

import configparser
from colorama import Fore

config = configparser.ConfigParser()
config.read(f'scripts/post/config/{__name__}.ini')

cfg = config.getint('config', 'cfg')
reverse = config.getboolean('config', 'reverse')

def print_post(posts):
    """
    Print the text of each post in the given list.

    Args:
        posts (list): A list of post objects.

    Returns:
        None
    """
    feed = posts.feed
    if reverse:
        feed = reversed(feed)

    for post in feed:
        replaced_post_text = post.post.record.text.replace("\n", f"{Fore.YELLOW}\\n{Fore.RESET}")
        print(f"{replaced_post_text}")