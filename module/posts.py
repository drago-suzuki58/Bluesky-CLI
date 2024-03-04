async def post(client):
    print("'\\n' is a newline character. Use it to create a new line in your post.")
    text = input("\nEnter your post: ")
    formatted_text = text.replace("\\n", "\n")

    responcse = await client.post(text=formatted_text)
    print(responcse) #!debug