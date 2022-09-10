import time 
######################################################### multiprocess #########################################################

from multiprocessing import Pool

# COUNT = 50000000
# def countdown(n):
#     while n>0:
#         n -= 1

# if __name__ == '__main__':
#     pool = Pool(processes=2)
#     start = time.time()
#     r1 = pool.apply_async(countdown, [COUNT//2])
#     r2 = pool.apply_async(countdown, [COUNT//2])
#     pool.close()
#     pool.join()
#     end = time.time()
#     print('Time taken in seconds -', end - start)



######################################################### multi_threaded.py #########################################################
from threading import Thread

# COUNT = 50000000

# def countdown(n):
#     while n>0:
#         n -= 1

# t1 = Thread(target=countdown, args=(COUNT//2,))
# t2 = Thread(target=countdown, args=(COUNT//2,))

# start = time.time()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end = time.time()

# print('Time taken in seconds -', end - start)