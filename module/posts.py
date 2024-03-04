async def post(client):
    print("'\\n' is a newline character. Use it to create a new line in your post.")
    text = input("\nEnter your post: ")
    formatted_text = text.replace("\\n", "\n")

    response = await client.post(text=formatted_text)
    print(response) #!debug

async def get_feed(client):
    feed = await client.get_author_feed(actor=client.me.handle)
    for post in feed:
        print(post) #!debug