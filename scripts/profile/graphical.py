import ascii_magic
import configparser

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