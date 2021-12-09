# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:14:23 2021

@author: black
"""

#WORKS! Note: need to rn on anaconda cmd (both scripts)
import os
import torch.multiprocessing as mp
os.environ['SET_NUM_THREADS'] = '1'

def worker(name):
  print(f"hello {name}")

if __name__ == "__main__":
  #mp.set_start_method('spawn')
  process = mp.Process(target=worker, args=('date' , ))
  process.start()
  process.join()  #so that main process doesnt end before child process


# WORKS!
#import multiprocessing
#import sys
#def print_cube(num):
#    """
#    function to print cube of given num
#    """
#    print("Cube: {}".format(num * num * num), flush=True)
#  
#def print_square(num):
#    """
#    function to print square of given num
#    """
#    print("Square: {}".format(num * num))
#  
#if __name__ == "__main__":
#    print('wat')
#    # creating processes
#    p1 = multiprocessing.Process(target=print_square, args=(10, ))
#    p2 = multiprocessing.Process(target=print_cube, args=(10, ))
#  
#    # starting process 1
#    p1.start()
#    # starting process 2
#    p2.start()
#  
#    # wait until process 1 is finished
#    p1.join()
#    # wait until process 2 is finished
#    p2.join()
#  
#    # both processes finished
#    print("Done!")
    


