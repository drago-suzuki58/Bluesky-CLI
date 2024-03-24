import importlib

import module.configs as configs

# スクリプトフォルダから動的にスクリプトを読み込ませる
config = configs.load_config()
post_script = importlib.import_module(f"scripts.post.{config['post_script']}")

async def post(client):
    print("'\\n' is a newline character. Use it to create a new line in your post.")
    text = input("\nEnter your post: ")
    formatted_text = text.replace("\\n", "\n")

    response = await client.post(text=formatted_text, langs=[config['post_language']])
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