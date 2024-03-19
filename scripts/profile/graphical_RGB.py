from bs4 import BeautifulSoup
import re
import ascii_magic
import configparser
from colorama import Fore

from scripts.module import image

config = configparser.ConfigParser()
config.read(f'scripts/profile/config/graphical_RGB.ini')

banner_columns = config.getint('config', 'banner_columns')
avatar_columns = config.getint('config', 'avatar_columns')

def print_profile(profile):
    profile_text = profile.description.split('\n')

    # banner
    banner_image = ascii_magic.from_url(profile.banner)
    banner_html = banner_image.to_html(columns=banner_columns)
    banner_colorized_html = image.colorize_html(banner_html)
    for line in banner_colorized_html.split('\n'):
        print(line)
    print()

    # avatar
    avatar_image = ascii_magic.from_url(profile.avatar)
    avatar_html = avatar_image.to_html(columns=avatar_columns)
    avater_colorized_html = image.colorize_html(avatar_html)

    for i, line in enumerate(avater_colorized_html.split('\n')):
        print(line, end='\t')
        if i == 1:
            print(f"{profile.display_name}")
        elif i == 2:
            print(f"{profile.handle}")
        elif i == 3:
            print(f"Total posts:{profile.posts_count}")
        elif i == 4:
            print(f"Followers:{profile.followers_count}\tFollowing:{profile.follows_count}")
        elif i >= 6 and i < 6 + len(profile_text):
            print(profile_text[i - 6])
        else:
            print()

def print_user_info(users, attribute_name):
    for user in getattr(users, attribute_name):
        if user.description is not None:
            replaced_user_description = user.description.replace("\n", f"{Fore.YELLOW}\\n{Fore.RESET}")
            print(f"{user.display_name}(@{user.handle})\n{replaced_user_description}\n")
        else:
            print(f"{user.display_name}(@{user.handle})\n--No description available--\n")

def print_followers(followers):
    print_user_info(followers, 'followers')

def print_following(following):
    print_user_info(following, 'follows')