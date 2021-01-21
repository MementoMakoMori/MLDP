import time as t
from multiprocessing import Pool
# def times_two(x):
#     return x*2
# def lazy_map(xs):
#     return list(map(times_two, xs))
# def parallel_map(xs, chunk):
#     with Pool(2) as P:
#         x = P.map(times_two, xs, chunk)
#     return x
# for i in range(0,7):
#     N = 10**i
#     t1 = time.time()
#     lazy_map(range(N))
#     lm_time = time.time() - t1
#     if N >= 100:
#         ch = N//4
#     else: ch = 1
#     t1 = time.time()
#     parallel_map(range(N), ch)
#     par_time = time.time() - t1
#     print("""
# -- N = {} --
# Lazy map time: {}
# Parallel map time: {}
# """.format(N,lm_time, par_time))

def vectOrder(vlist: list):
    return sorted(vlist, reverse=True)
def lazy_map(vs: list):
    return list(map(vectOrder, vs))
def parallel_map(vs: list):
    with Pool(2) as P:
        x = P.map(vectOrder, vs)
    return x
def more_par_map(vs: list):
    with Pool(4) as P:
        x = P.map(vectOrder, vs)
    return x

for i in range(0,7):
    n = 10**i
    N = [list(range(n))]*32
    t1 = t.time()
    lazy_map(N)
    lm_time = t.time() - t1
    # if n >= 100:
    #     ch = n//4
    # else: ch = 1
    t1 = t.time()
    parallel_map(N)
    par_time = t.time() - t1
    t1 = t.time()
    more_par_map(N)
    more_par_time = t.time() - t1
    print("""
-- N = {} --
Lazy map time: {}
Parallel map time (2): {}
Par map time (4): {}
""".format(n,lm_time, par_time, more_par_time))


