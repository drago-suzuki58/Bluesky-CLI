import asyncio

from module.login import login
from module.commands import commands

async def main():
    client = await login()
    await commands(client)

if __name__ == '__main__':
    asyncio.run(main())