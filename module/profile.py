import configparser
import importlib

config = configparser.ConfigParser()
config.read('config/config.ini')

profile_script_name = config['script']['profile_script']
profile_script = importlib.import_module(f"scripts.profile.{profile_script_name}")

async def get_profile(client, handle):
    profile = await client.get_profile(actor=handle)
    profile_script.print_profile(profile)