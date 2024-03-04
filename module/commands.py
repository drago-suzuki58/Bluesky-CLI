import asyncio

import module.posts as posts

async def commands(client):
    while True:
        user_input = input("BlueSky>>")

        if user_input == "help":
            print("""
post: Create a new post
help: Shows this message
exit: Exits the program
""")
        elif user_input == "post":
            await posts.post(client)

        elif user_input == "exit":
            print("See you later!")
            break

        else:
            print("\033[31m","Unknown command. Type 'help' for a list of commands.","\033[0m")

    return asyncio.sleep(1)
