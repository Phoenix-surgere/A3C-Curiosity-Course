# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:14:23 2021

@author: black
"""

#WORKS! Note: need to rn on anaconda cmd (both scripts)
import os
import torch.multiprocessing as mp
import gym
import numpy as np

os.environ['SET_NUM_THREADS'] = '2'


class RandomAgent():
  def __init__(self, env):
    self.env = env
    self.env.reset()

  def choose_action(self):
    action = self.env.action_space.sample()
    return action


def worker():
  env = gym.make('CartPole-v0')
  agent = RandomAgent(env)
  print("ID of process running worker1: {}".format(os.getpid()))
  n_eps = 5
  scores = []
  for i in range(n_eps):
    done, state, score = False, env.reset(), 0
    while not done:
      action = agent.choose_action()
      next_state, reward, done, _ = env.step(action)
      score += reward
    scores.append(score)
  print(f"Score of agent id:{os.getpid()}: {np.mean(scores)}")

  
if __name__ == "__main__":
    print('Multithreading Initiated...')
    # creating processes
    p1 = mp.Process(target=worker)
    p2 = mp.Process(target=worker)
    p3 = mp.Process(target=worker)

    # starting process 1
    p1.start()
    p2.start()
    p3.start()

    print("ID of process p1: {}".format(p1.pid))
    print("ID of process p2: {}".format(p2.pid))
    print("ID of process p3: {}".format(p3.pid))

    # wait until process 1 is finished
    p1.join()
    p2.join()
    p3.join()

    #both processes finished
    print("Done!")


