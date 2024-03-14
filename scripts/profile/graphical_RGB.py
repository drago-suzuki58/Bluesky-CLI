from math import e
from bs4 import BeautifulSoup
import re
import ascii_magic
import configparser
from colorama import Fore

config = configparser.ConfigParser()
config.read(f'scripts/profile/config/graphical_RGB.ini')

banner_columns = config.getint('config', 'banner_columns')
avatar_columns = config.getint('config', 'avatar_columns')

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def colorize_string_hex(s, hex_color):
    r, g, b = hex_to_rgb(hex_color)
    return f'\033[38;2;{r};{g};{b}m{s}\033[0m'

def extract_color_and_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    color_text_pairs = []

    for tag in soup.find_all(['span', 'br']):
        if tag.name == 'br':
            color_text_pairs.append(('\n', ''))
            continue

        style = tag.get('style')
        if style:
            color = re.search(r'color: #([A-Fa-f0-9]{6})', style)
            if color:
                color_text_pairs.append((color.group(1), tag.text))

    return color_text_pairs

def colorize_html(html):
    color_text_pairs = extract_color_and_text(html)
    result = ""
    for hex_color, text in color_text_pairs:
        if hex_color == '\n':
            result += '\n'
        else:
            result += colorize_string_hex(text, hex_color)
    return result

def print_profile(profile):
    profile_text = profile.description.split('\n')

    # banner
    banner_image = ascii_magic.from_url(profile.banner)
    banner_html = banner_image.to_html(columns=banner_columns)
    banner_colorized_html = colorize_html(banner_html)
    for line in banner_colorized_html.split('\n'):
        print(line)
    print()

    # avatar
    avatar_image = ascii_magic.from_url(profile.avatar)
    avatar_html = avatar_image.to_html(columns=avatar_columns)
    avater_colorized_html = colorize_html(avatar_html)

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