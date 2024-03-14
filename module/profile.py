import configparser
import importlib

config = configparser.ConfigParser()
config.read('config/config.ini')

profile_script_name = config['script']['profile_script']
profile_script = importlib.import_module(f"scripts.profile.{profile_script_name}")

async def get_profile(client, handle):
    profile = await client.get_profile(actor=handle)
    profile_script.print_profile(profile)

async def print_followers(client, handle):
    followers = await client.get_followers(handle)
    profile_script.print_followers(followers)

async def print_following(client, handle):
    following = await client.get_follows(handle)
    profile_script.print_following(following)