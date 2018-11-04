import numpy as np
import random

class MultiArmBandit:
    
    def __init__(self, arms):
        self.arms = arms
        self.bandit_matrix = np.random.rand(self.arms, self.arms)
        self.update_state()
        
    def get_state(self):
        return self.state
    
    def update_state(self):
        self.state = np.random.randint(0, self.arms)
        
    def pull_arm_and_get_reward(self, arm):
        probability = self.bandit_matrix[self.get_state()][arm]
        reward = 0
        for _ in range(self.arms):
            if random.random() < probability:
                reward += 1
    
        self.update_state()
        return reward