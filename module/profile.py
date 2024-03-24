import configparser
import importlib

import module.configs as configs

config = configs.load_config()
profile_script = importlib.import_module(f"scripts.profile.{config['profile_script']}")

async def get_profile(client, handle):
    profile = await client.get_profile(actor=handle)
    profile_script.print_profile(profile)

async def print_followers(client, handle):
    followers = await client.get_followers(handle)
    profile_script.print_followers(followers)

async def print_following(client, handle):
    following = await client.get_follows(handle)
    profile_script.print_following(following)