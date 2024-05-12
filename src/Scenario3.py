# Scenario 3 for CSC3022F ML Assignment 2
# Find 3 boxes in order (RED, GREEN, BLUE)
# Mahir Moodaley (MDLMAH007)
# 11 May 2024

from FourRooms import FourRooms
import numpy as np

aTypes = ['UP', 'DOWN', 'LEFT', 'RIGHT']
gTypes = ['EMPTY', 'RED', 'BLUE', 'GREEN']    

# func to choose action using epsilon-greedy policy
def choose_action(Q, state, epsilon):
    if np.random.uniform(0, 1) < epsilon:
        return np.random.choice([FourRooms.UP, FourRooms.DOWN, FourRooms.LEFT, FourRooms.RIGHT])  # choose random action
    else:
        # select action with highest Q-value at given state
        q_values = Q[state[0], state[1]]
        return np.argmax(q_values)

# calculates the reward at a given point, depending on how many packages have been collected, and how many steps have been taken,
# and if the state has been visited before
def calc_reward(packages_left, steps, visited_states, state, grid_type, finished):
    reward = 0 # base reward
    step_penalty = -0.1 # negative reward for every step
    r_per_package = 1000 # reward per package
    visited_state_penalty = -10
    early_stop_penalty = -10000000000
    
    #if grid_type == FourRooms.RED and packages_left == 2:
    if grid_type == FourRooms.GREEN and packages_left > 1:
        reward += early_stop_penalty
    elif grid_type == FourRooms.BLUE and packages_left > 0:
        reward += early_stop_penalty * 1000
    elif  grid_type == FourRooms.RED:
        reward += r_per_package * 1000
    if (state[0], state[1]) in visited_states:
        reward += visited_state_penalty        
    # calculate the total reward
    reward += ((3 - packages_left) * r_per_package) + (steps * step_penalty)
    return reward

def calculate_reward(grid_type, visited_states, steps_taken, packages_collected, state):
    reward = 0
    reward_per_package = 100  # Reward for each package collected
    penalty_per_step = -1  # Penalty for each step taken
    penalty_per_visited_cell = -10  # Penalty for revisiting a cell

    if grid_type == FourRooms.RED and packages_collected == 0:
        reward += reward_per_package
    elif grid_type == FourRooms.GREEN and packages_collected == 1:
        reward += reward_per_package
    elif grid_type == FourRooms.BLUE and packages_collected == 2:
        reward += reward_per_package
    else:
        reward += penalty_per_visited_cell

    reward += penalty_per_step*steps_taken

    if (state[0], state[1]) in visited_states:
        reward += penalty_per_visited_cell

    return reward

def main():   
    # Create FourRooms Object
    fourRoomsObj = FourRooms('rgb')

    # Q-learning parameters
    alpha = 0.1  # learning rate
    gamma = 0.9  # discount factor
    epsilon = 0.5  # for epsilon-greedy policy
    epochs = 1000  # num times to do training

    # init Q table with zeros
    Q = np.zeros((12, 12, 4)) 

    # training
    for epoch in range(epochs):
        fourRoomsObj.newEpoch()
        
        state = fourRoomsObj.getPosition()
        finished = False
        visited_states = set()
        
        steps_taken = 0 # track how many steps have been taken
        while not finished:
            # choose action
            action = choose_action(Q, state, epsilon)
            # take action and get new state and reward
            grid_type, new_state, packages_left, is_terminal = fourRoomsObj.takeAction(action)
            
            # check if terminal state has been reached
            if is_terminal:
                finished = True            

            # define reward
            reward = calc_reward(packages_left, steps_taken, visited_states, new_state, grid_type, finished)
            #reward = calculate_reward(grid_type, visited_states, steps_taken, packages_left, new_state)
            steps_taken += 1

            # update Q-value using Q-learning equation
            Q[state[0], state[1], action] += alpha * (reward + gamma * np.max(Q[new_state[0], new_state[1]]) - Q[state[0], state[1], action])
            
            visited_states.add((state[0], state[1]))
            
            #print("Agent took {0} action and moved to {1} of type {2} there are {3} packages left".format(aTypes[action], new_state, gTypes[grid_type],packages_left))

            state = new_state
            

    # Show Path
    fourRoomsObj.showPath(-1)

if __name__ == "__main__":
    main()