import numpy as np
import matplotlib.pyplot as plt
from time import process_time_ns as ts


maxiterations = 100
def fc(zc, c): return zc**2 + c



def reg_mandlebrot(aryNN):
  aryXX = np.linspace(-1.5, 0.5, aryNN)
  aryYY = np.linspace(-1, 1, aryNN)
  results = [[0 for i in range(len(aryYY))] for j in range(len(aryXX))]
  for i in range(len(aryXX)):
    for j in range(len(aryYY)):
        k = 0
        z = 0 + 0j
        c_ij = aryXX[i] + aryYY[j] * 1j
        while (abs(z) < 2 and k < maxiterations):
            z = fc(z, c_ij)
            k = k+1
            results[j][i] = k
  return results

def reg_timing_mandlebrot(aryNN):
  start_time_ns = ts()
  reg_mandlebrot(aryNN)
  end_time_ns = ts()
  return end_time_ns - start_time_ns
  
def reg_mandlebrot_plot(aryNN):
  results = reg_mandlebrot(aryNN)
  plt.pcolormesh(results)
  plt.show()

#if __name__ == '__main__':
#  reg_mandlebrot_plot(1000)