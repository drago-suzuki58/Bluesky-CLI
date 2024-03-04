from atproto import AsyncClient
import configparser

async def login():
    client = AsyncClient()

    config = configparser.ConfigParser()
    config.read('config/config.ini')

    if 'save' in config and config['save']['username'] != "username" and config['save']['password'] != "password":
        username = config['save']['username']
        password = config['save']['password']
        try:
            profile = await client.login(username, password)
        except Exception as e:
            print("Login failed: ")
            return
        print("Login successful!\n", profile.display_name)
    else:
        username = input("Your Username: ")
        password = input("Your password: ")
        try:
            profile = await client.login(username, password)
        except Exception as e:
            print("Login failed: ")
            return
        print("Login successful!\n", profile.display_name)

    print("\033[38;5;33m" ,
        " ,////                            .//// ", "\033[32m", " _     _  _______  ___      _______  _______  __   __  _______    _______  _______ \n", "\033[38;5;33m"
        "//////////                    */////////", "\033[32m", "| | _ | ||       ||   |    |       ||       ||  |_|  ||       |  |       ||       |\n", "\033[38;5;33m"
        "////////////*               ////////////", "\033[32m", "| || || ||    ___||   |    |       ||   _   ||       ||    ___|  |_     _||   _   |\n", "\033[38;5;33m"
        "//////////////,           //////////////", "\033[32m", "|       ||   |___ |   |    |       ||  | |  ||       ||   |___     |   |  |  | |  |\n", "\033[38;5;33m"
        "/////////////////       ////////////////", "\033[32m", "|       ||    ___||   |___ |      _||  |_|  ||       ||    ___|    |   |  |  |_|  |\n", "\033[38;5;33m"
        " /////////////////.   /////////////////,", "\033[32m", "|   _   ||   |___ |       ||     |_ |       || ||_|| ||   |___     |   |  |       |\n", "\033[38;5;33m"
        " //////////////////////////////////////*", "\033[32m", "|__| |__||_______||_______||_______||_______||_|   |_||_______|    |___|  |_______|\n", "\033[38;5;33m"
        "  ////////////////////////////////////. ", "\033[32m", " _______  ___      __   __  _______  _______  ___   _  __   __ \n", "\033[38;5;33m"
        "    .///////////////////////////////    ", "\033[32m", "|  _    ||   |    |  | |  ||       ||       ||   | | ||  | |  |\n", "\033[38;5;33m"
        "       //////////////////////////.      ", "\033[32m", "| |_|   ||   |    |  | |  ||    ___||  _____||   |_| ||  |_|  |\n", "\033[38;5;33m"
        "    .///////////////////////////////    ", "\033[32m", "|       ||   |    |  |_|  ||   |___ | |_____ |      _||       |\n", "\033[38;5;33m"
        "    .///////////////////////////////    ", "\033[32m", "|  _   | |   |___ |       ||    ___||_____  ||     |_ |_     _|\n", "\033[38;5;33m"
        "     //////////////  ,/////////////     ", "\033[32m", "| |_|   ||       ||       ||   |___  _____| ||    _  |  |   |  \n", "\033[38;5;33m"
        "        /////////      *////////*       ", "\033[32m", "|_______||_______||_______||_______||_______||___| |_|  |___|  \n", "\033[0m")

    if config["save"]["save"] == "0":
        while True:
            save = input("Do you want to save your login info? (y/n): ")
            if save == "y":
                config = configparser.ConfigParser()
                config['save'] = {'username': username, 'password': password, 'save': "1"}
                with open('config/config.ini', 'w') as f:
                    config.write(f)
                print("Login info saved!")
                break
            elif save == "n":
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    return client