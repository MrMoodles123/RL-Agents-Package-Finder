# Reinforcement Learning Grid World

This project contains python code for RL agents that pick up objects in a grid world in 3 different scenarios.

## Setup
The environment is a 2D grid-world of size 13 × 13 but rows 0 and 12 and columns 0 and 12 are boundaries. The environment has one start state that is randomly assigned when the environment is created and a terminal state that is determined when the number of packages left to collect reaches 0.

The agents only have a partial representation of the environment which consists of their location (x, y) and the number of packages left k. They don't know the location of the package(s), hallways or the boundaries of the environment.

The agent has 4 actions: UP, DOWN, LEFT, RIGHT.

A suitable reward function has been designed for each scenario such that the agents produce the expected behaviour for each scenario. 

The goal of each Agent is to derive an optimal policy such that it collects all of the packages in the environment in accordance with each scenario description.

## Scenario 1

The Agent must collect 1 package located somewhere in the environment.

## Scenario 2

The Agent must collect 3 packages located somewhere in the environment.

## Scenario 3

The Agent must collect 3 packages located somewhere in the environment. These packages are marked as red (R), green (G) and blue (B) and must be collected in that order. Collecting a package in the wrong order will terminate a simulation early.

## How To Run

A makefile has been provided to install depedencies, start a virtual environment and run each python file.

## Template

The provided code was FourRooms.py and ExecutionSkeleton.py from [this paper](http://arxiv.org/abs/1906.10667). The code was not modified at all.
