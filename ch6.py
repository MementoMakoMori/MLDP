import time as t
from multiprocessing import Pool
from statistics import mean
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

def longerFunct(vlist: list) -> list:
    vars = sorted(vlist, reverse = True)
    for k in range(len(vars)):
        vars[k] = k*100
    for k in range(len(vars)):
        vars[k] = k/5
    for k in range(len(vars)):
        if k % 2 == 0:
            vars[k] = True
        else: vars[k] = False
    for k in range(len(vars)):
        vars[k] = int(vars[k]) + 1
        vars[k] = ord(str(vars[k]))
    return vars

def lazy_map(vs: list, funct):
    return list(map(funct, vs))

def parallel_map(vs: list, funct):
    with Pool(2) as P:
        x = P.map(funct, vs)
    return x

def more_par_map(vs: list, funct):
    with Pool(4) as P:
        x = P.map(funct, vs)
    return x

with open('./speedTests', 'w') as st:
    functs = [vectOrder, longerFunct]
    for a in functs:
        if a == vectOrder: fname = 'Simple'
        else: fname = 'Longer'
        for i in range(4,7):
            lm_time = []
            par_time = []
            more_par_time = []
            n = 10**i
            N = [list(range(n))]*64
            for j in range(10):
                t1 = t.time()
                lazy_map(N, a)
                lm_time.append(t.time() - t1)
            for j in range(10):
                t1 = t.time()
                parallel_map(N, a)
                par_time.append(t.time() - t1)
            for j in range(10):
                t1 = t.time()
                more_par_map(N, a)
                more_par_time.append(t.time() - t1)
            st.write("""
        Function: {}
        -- N = {} --
        Lazy map mean time: {}
        Lazy map min time: {}\n
        Par map mean time (2): {}
        Par map min time (2): {}\n
        Par map mean time (4): {}
        Par map min time (4): {}\n
        """.format(fname, n, mean(lm_time), min(lm_time), mean(par_time), min(par_time), mean(more_par_time), min(more_par_time)))
            print("Completed {} Test, N = {}".format(fname, n))
    st.close()

