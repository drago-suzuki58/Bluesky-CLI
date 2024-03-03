import asyncio

from module.login import login

async def main():
    await login()

if __name__ == '__main__':
    asyncio.run(main())