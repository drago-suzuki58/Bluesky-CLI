import module.posts as posts

HELP_MESSAGE = """
post: Create a new post

get
    feed: Get BlueSky feed
    post: Get specific posts
    user: Get specific user's profile
help: Shows this message
exit: Exits the program
"""

async def commands(client):
    while True:
        user_input = input("BlueSky>>")

        if user_input == "help":
            print(HELP_MESSAGE)

        elif user_input == "post":
            await posts.post(client)

        elif user_input.startswith("get feed"):
            await posts.get_feed(client)

        elif user_input.startswith("get tl"):
            await posts.get_timeline(client)

        elif user_input == "exit":
            print("See you later!")
            break

        else:
            print("\033[31m","Unknown command. Type 'help' for a list of commands.","\033[0m")
