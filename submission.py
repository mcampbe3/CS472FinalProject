"""
CIS 472 Final Project: Kaggle Connect X Competition

Date Last Modified: 3/10/2020

Authors: Mikayla Campbell, James Kang, Olivia Pannell
"""

# Create ConnectX environment
from kaggle_environments import evaluate, make, utils

env = make("connectx", debug=True)
env.render()

def act(observation, configuration):
    board = observation.board
    columns = configuration.columns
    return [c for c in range(columns) if board[c] == 0][0]


# Create an agent
def my_agent(observation, configuration):
	from random import choice
	return choice([c for c in range(configuration.columns) if observation.board[c] == 0])


# Test your agent
env.reset()
env.run([my_agent, "random"])
env.render(mode="ipython", width=500, height=450)

# Debug/Train your agent
trainer = env.train([None, "random"])

observation = trainer.reset()

while not env.done:
	my_action = my_agent(observation, env.configuration)
	print("My Action", my_action)
	observation, reward, done, info = trainer.step(my_action)
env.render()

# Evaluate your agent
def mean_reward(rewards):
	return (r[0] for r in rewards) / sun(r[0] + r[1] for r in rewards)

# print("My Agent vs Random Agent:", mean_reward(evaluate("connect x", [my_agent, "random"], num_episodes=10)))
# print("My Agent vs Negmax Agent:", mean_reward(evaluate("connect x", [my_agent, "negamax"], num_episodes=10)))

# Play your agent
env.play([my_agent, None], width=500, height=450)

import inspect
import os

def write_agent_to_file(function, file):
    with open(file, "a" if os.path.exists(file) else "w") as f:
        f.write(inspect.getsource(function))
        print(function, "written to", file)

write_agent_to_file(my_agent, "submission.py")

import sys
out = sys.stdout
submission = utils.read_file("/kaggle/working/submission.py")
agent = utils.get_last_callable(submission)
sys.stdout = out

env = make("connectx", debug=True)
env.run([agent, agent])
print("Success!" if env.state[0].status == env.state[1].status == "DONE" else "Failed...")



def my_agent(observation, configuration):
	from random import choice
	return choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(observation, configuration):
	from random import choice
	return choice([c for c in range(configuration.columns) if observation.board[c] == 0])
