import socket, traceback
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import csv

import numpy as np
import numpy as np
from scipy.interpolate import make_interp_spline



host = '192.168.7.54'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))


k=15


def animate():
    index = count()

    x_vals = []
    y_vals = []
    z_vals = []
    with open('a.txt', 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')

        for row in lines:
          x_vals.append(row[2])

          y_vals.append(row[3])

          z_vals.append(row[4])


    #print(x_vals)
    plt.cla()

    plt.plot(x_vals,y_vals, label='X vs Y')
    plt.plot(x_vals,z_vals, label='X vs Z')

    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()
    plt.close()




while 1:

      while(k):
           message, address = s.recvfrom(8192)
           print(message)
           message = str(message)

           f = open("a.txt", "a")
           f.write(message + "\n")
           k -= 1
      f.close()
      animate()
      k=15









