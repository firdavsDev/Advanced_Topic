"""

    Using JobLib( pip install joblib_)

"""
import math
from joblib import Parallel, delayed

# results = [math.factorial(x) for x in range(10000)] # 10 secund 

# n_jobs is core. if -1 all core
results = Parallel(n_jobs=-1)(delayed(math.factorial)(x) for x in range(10_000)) #6 secund in 2core.  



#multiprocesseing (Poolm .map()) use 100% core
#Thread #GIL lock
#asycio - Good at I/O 