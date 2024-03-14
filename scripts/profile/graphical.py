import ascii_magic
import configparser
from colorama import Fore

config = configparser.ConfigParser()
config.read(f'scripts/profile/config/graphical.ini')

banner_columns = config.getint('config', 'banner_columns')
avatar_columns = config.getint('config', 'avatar_columns')

def print_profile(profile):
    print(f"avatarURL: {profile.avatar}")

    # banner
    banner_image = ascii_magic.from_url(profile.banner)
    banner_image.to_terminal(columns=banner_columns,)

    # avatar
    avatar_image = ascii_magic.from_url(profile.avatar)
    avatar_image.to_terminal(columns=avatar_columns)

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