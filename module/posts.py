import configparser
import importlib

# スクリプトフォルダから動的にスクリプトを読み込ませる
config = configparser.ConfigParser()
config.read('config/config.ini')

post_script_name = config['script']['post_script']
post_language = config['config']['post_language']

post_script = importlib.import_module(f"scripts.post.{post_script_name}")

async def post(client):
    print("'\\n' is a newline character. Use it to create a new line in your post.")
    text = input("\nEnter your post: ")
    formatted_text = text.replace("\\n", "\n")

    response = await client.post(text=formatted_text, langs=[post_language])
    print(response) #!debug

async def get_feed(client, handle):
    try:
        feed = await client.get_author_feed(actor=handle)
        post_script.print_post(feed)
    except Exception as e:
        print(f"An error occurred: {e}")

async def get_timeline(client):
    try:
        timeline = await client.get_timeline()
        post_script.print_post(timeline)
    except Exception as e:
        print(f"An error occurred: {e}")