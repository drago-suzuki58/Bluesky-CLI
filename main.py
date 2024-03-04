import asyncio

from module.login import login
from module.commands import commands

async def main():
    try:
        client = await login()
        await commands(client)
    except Exception as e:
        print(f"An error occurred: {e}") #!debug

if __name__ == '__main__':
    asyncio.run(main())