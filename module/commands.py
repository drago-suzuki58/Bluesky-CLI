import sys
from tkinter import E

import module.posts as posts
import module.profile as profile

HELP_MESSAGE = """
post : Create a new post

get
    feed : Get User's feed
    tl : Get User's timeline
    profile <handle> : Get specific user's profile
    followers <handle> : Get specific user's followers
    following <handle> : Get specific user's following

help : Shows this message

restart : Restarts this program(Only when started from bat file)

exit : Exits the program
"""

ERROR_HANDLE_MESSAGE = "\033[31mError: No handle specified. Please type handle.\033[0m"

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
                print(ERROR_HANDLE_MESSAGE)
            else:
                try:
                    await profile.get_profile(client, handle)
                except Exception as e:
                    print(f"HANDLE: {handle} is not found.")

        elif user_input.startswith("get followers"):
            handle = user_input.split(" ")[-1]
            if handle == "followers":
                print(ERROR_HANDLE_MESSAGE)
            else:
                try:
                    await profile.print_followers(client, handle)
                except Exception as e:
                    print(f"HANDLE: {handle} is not found.")

        elif user_input.startswith("get following"):
            handle = user_input.split(" ")[-1]
            if handle == "following":
                print(ERROR_HANDLE_MESSAGE)
            else:
                try:
                    await profile.print_following(client, handle)
                except Exception as e:
                    print(f"HANDLE: {handle} is not found.")

        elif user_input == "restart":
            print("Restarting...Please wait...")
            sys.exit(0)

        elif user_input == "exit":
            print("See you later!")
            sys.exit(1)

        else:
            print("\033[31m","Unknown command. Type 'help' for a list of commands.","\033[0m")
