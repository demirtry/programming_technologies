import threading
import time
import multiprocessing
import requests
import asyncio
import aiohttp


# список url
urls = ['https://www.example.com'] * 10


def fetch_url(url):
    response = requests.get(url)
    return response.text


def sequence():
    start_time = time.time()
    for url in urls:
        fetch_url(url)
    end_time = time.time()
    print(f'sequence time: {end_time - start_time: 0.2f} \n')


def threads():
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f'threads time: {end_time - start_time: 0.2f} \n')


def processes():
    start_time = time.time()
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=fetch_url, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    end_time = time.time()
    print(f'processes time: {end_time - start_time: 0.2f} \n')


async def fetch_url_async(session, url):
    async with session.get(url) as response:
        return await response.text()


async def asyncio_func():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url_async(session, url) for url in urls]
        await asyncio.gather(*tasks)
    end_time = time.time()
    print(f'asyncio time: {end_time - start_time: 0.2f} \n')


if __name__ == '__main__':
    sequence()
    threads()
    processes()

    asyncio.run(asyncio_func())

    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):
        
        sequence time:  5.89

        threads time:  0.60
        
        processes time:  1.48
        
        asyncio time:  0.61
    """
