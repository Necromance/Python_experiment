# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:42:25 2017

@author: Necromancer
"""

import numpy as np
import random
import matplotlib.pyplot as plt

gamma = 0.8


reward = np.array([[0,-10,0,-1,-1],
                   [0,10,-1,0,-1],
                   [-1,0,0,10,-1],
                   [-1,0,-10,0,10]])
q_matrix = np.zeros((4,5))

transition_matrix = np.array([[-1,2,-1,1,1],
                              [-1,3,0,-1,2],
                              [0,-1,-1,3,3],
                              [1,-1,2,-1,4]])

valid_actions = np.array([[1,3,4],
                         [1,2,4],
                         [0,3,4],
                         [0,2,4]])


for i in range(1000):
    start_state = 0
    current_state = start_state
    while current_state != 3:
        action = random.choice(valid_actions[current_state])
        next_state = transition_matrix[current_state][action]
        future_rewards = []
        for action_nxt in valid_actions[next_state]:#到达下一个状态后有多种选择，计算reward然后在选reward最大的那个
            future_rewards.append(q_matrix[next_state][action_nxt])
        q_state = reward[current_state][action] + gamma*max(future_rewards)
        q_matrix[current_state][action] = q_state
        print(q_matrix)
        current_state = next_state
        if current_state == 3:
            print('goal state reached')
print('final q-matrix :')
print(q_matrix)
