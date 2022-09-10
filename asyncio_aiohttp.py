import asyncio
import time
from pathlib import Path
import aiohttp


URL = 'https://cataas.com/cat'
CATS_WE_WANT = 100
OUT_PATH = Path(__file__).parent / 'cats'
OUT_PATH.mkdir(exist_ok=True, parents=True)
OUT_PATH = OUT_PATH.absolute()


async def get_cat(client: aiohttp.ClientSession, idx: int) -> bytes:
    async with client.get(URL) as response:
        print(response.status)
        result = await response.read()
        await write_to_disk(result, idx)


async def write_to_disk(content: bytes, id: int):
    file_path = f"{OUT_PATH}/{id}.png"
    with open(file_path, mode='wb') as f:
        f.write(content)


async def get_all_cats():
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(15)) as client:
        tasks = [asyncio.create_task(get_cat(client=client, idx=i)) for i in range(CATS_WE_WANT)]
        return await asyncio.gather(*tasks)


def main():
    res = asyncio.get_event_loop().run_until_complete(get_all_cats())
    print(len(res))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f"Runtime of the program is {end - start}")
