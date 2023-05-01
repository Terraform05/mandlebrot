from multiprocessing import Pool
from multiprocessing import cpu_count
import numpy as np
import matplotlib.pyplot as plt
from time import process_time_ns as ts


maxiterations = 100
def fc(zc, c): return zc**2 + c


def process(ijarys):
    i, j, aryXX, aryYY = ijarys
    k = 0
    z = 0 + 0j
    c_ij = aryXX[i] + aryYY[j] * 1j
    while (abs(z) < 2 and k < maxiterations):
        z = fc(z, c_ij)
        k = k+1
    return (i, j, k)


def multiprocess_mandlebrot(aryNN, process_n=cpu_count()):
    aryXX = np.linspace(-1.5, 0.5, aryNN)
    aryYY = np.linspace(-1, 1, aryNN)
    results = [[0 for i in range(len(aryYY))] for j in range(len(aryXX))]
    with Pool(processes=process_n) as p:
        arg = ([(i, j, aryXX, aryYY) for i in range(len(aryXX))
               for j in range(len(aryYY))])
        rv = p.map(process, arg)
        for i, j, k in rv:
            results[j][i] = k
    return results


def mp_timing_mandlebrot(aryNN, process_n):
    start_time_ns = ts()
    multiprocess_mandlebrot(aryNN, process_n=process_n)
    end_time_ns = ts()
    return end_time_ns - start_time_ns


def multiproces_mandlebrot_plot(aryNN):
    results = multiprocess_mandlebrot(aryNN)
    plt.pcolormesh(results)
    plt.show()


# if __name__ == '__main__':
#    print('done')
