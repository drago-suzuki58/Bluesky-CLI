import sys

import module.posts as posts
import module.profile as profile

HELP_MESSAGE = """
post : Create a new post

get
    feed : Get User's feed
    tl : Get User's timeline
    profile <handle> : Get specific user's profile

help : Shows this message

restart : Restarts this program(Only when started from bat file)

exit : Exits the program
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

        elif user_input.startswith("get profile"):
            handle = user_input.split(" ")[-1]
            # handleが指定されていない場合は、handle=profileになるのでそれをエラーとして処理
            if handle == "profile":
                print("\033[31m","Error: No handle specified. Please type handle.","\033[0m")
            else:
                await profile.get_profile(client, handle)

        elif user_input == "restart":
            print("Restarting...Please wait...")
            sys.exit(0)

        elif user_input == "exit":
            print("See you later!")
            sys.exit(1)

        else:
            print("\033[31m","Unknown command. Type 'help' for a list of commands.","\033[0m")
