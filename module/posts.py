import configparser
import importlib

# スクリプトフォルダから動的にスクリプトを読み込ませる
config = configparser.ConfigParser()
config.read('config/config.ini')

post_script_name = config['script']['post_script']
post_script = importlib.import_module(f"scripts.post.{post_script_name}")

async def post(client):
    print("'\\n' is a newline character. Use it to create a new line in your post.")
    text = input("\nEnter your post: ")
    formatted_text = text.replace("\\n", "\n")

    response = await client.post(text=formatted_text)
    print(response) #!debug

async def get_feed(client):
    feed = await client.get_author_feed(actor=client.me.handle)
    post_script.print_post(feed)

async def get_timeline(client):
    timeline = await client.get_timeline()
    post_script.print_post(timeline)