# import concurrent.futures
# import requests
# import threading
# import time


# thread_local = threading.local()


# def get_session():
#     if not hasattr(thread_local, "session"):
#         thread_local.session = requests.Session()
#     return thread_local.session


# def download_site(url):
#     session = get_session()
#     with session.get(url) as response:
#         print(f"Read {len(response.content)} from {url}")


# def download_all_sites(sites):
#     with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#         executor.map(download_site, sites)


# if __name__ == "__main__":
#     sites = [
#         "https://www.jython.org",
#         "http://olympus.realpython.org/dice",
#     ] * 80
#     start_time = time.time()
#     download_all_sites(sites)
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} in {duration} seconds") # Downloaded 160 in 5.0503315925598145 seconds



############################################################################### Thread-local sessions ###############################################################################
# import threading
# import time

# total = 0
# lock = threading.Lock()

# def increment_n_times(n):
#     global total
#     for _ in range(n):
#         total += 1

# def safe_increment_n_times(n):
#     global total
#     for _ in range(n):
#         lock.acquire()
#         total += 1
#         lock.release()

# def increment_in_x_threads(x, func, n):
#     threads = [threading.Thread(target=func, args=(n,)) for _ in range(x)]
#     global total
#     total = 0
#     begin = time.time()
#     for thread in threads:
#         thread.start()
#     for thread in threads:
#         thread.join()
#     print(f'finished in {time.time() - begin}s.\ntotal: {total}\nexpected: {n * x}\ndifference: {n*x - total} ({100 - total/n/x*100} %)')

# print('unsafe:')
# increment_in_x_threads(70, increment_n_times, 100000)
# # unsafe:
# # finished in 0.3596229553222656s.
# # total: 6967844
# # expected: 7000000
# # difference: 32156 (0.4593714285714299 %)

# print('\nwith locks:')
# increment_in_x_threads(70, safe_increment_n_times, 100000)
# # with locks:
# # finished in 13.929630517959595s.
# # total: 7000000
# # expected: 7000000
# # difference: 0 (0.0 %)




############################################################################### Asyncio  ###############################################################################

# import asyncio
# import time
# import aiohttp #pip install aiohttp


# async def download_site(session, url):
#     async with session.get(url) as response:
#         print("Read {0} from {1}".format(response.content_length, url))


# async def download_all_sites(sites):
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for url in sites:
#             task = asyncio.ensure_future(download_site(session, url))
#             tasks.append(task)
#         await asyncio.gather(*tasks, return_exceptions=True)


# if __name__ == "__main__":
#     sites = [
#         "https://www.jython.org",
#         "http://olympus.realpython.org/dice",
#     ] * 80
#     start_time = time.time()
#     asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} sites in {duration} seconds") # Downloaded 160 sites in 1.516411304473877 seconds



############################################################################### MultiProcessing  ###############################################################################


''' run only on a single CPU or core in your computer. '''

# import requests
# import multiprocessing
# import time

# session = None


# def set_global_session():
#     global session
#     if not session:
#         session = requests.Session()


# def download_site(url):
#     with session.get(url) as response:
#         name = multiprocessing.current_process().name
#         print(f"{name}:Read {len(response.content)} from {url}")


# def download_all_sites(sites):
#     with multiprocessing.Pool(initializer=set_global_session) as pool:
#         pool.map(download_site, sites)


# if __name__ == "__main__":
#     sites = [
#         "https://www.jython.org",
#         "http://olympus.realpython.org/dice",
#     ] * 80
#     start_time = time.time()
#     download_all_sites(sites)
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} in {duration} seconds") # Downloaded 160 in 2.5645487308502197 seconds

