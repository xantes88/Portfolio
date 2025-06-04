Reinforcement Learning for Cybersecurity: SARSA and DDQN Agents
Overview
This project explores the application of Reinforcement Learning (RL) to develop defensive agents capable of countering cyberattacks. Two RL algorithms were implemented: SARSA, an on-policy method using a Q-table, and Double Deep Q-Network (DDQN), an off-policy deep learning-based approach. These agents were trained and evaluated using the gym-idsgame environment under two attack scenarios: random attack and maximal attack.

Table of Contents
Project Structure

SARSA Implementation

Algorithm Overview

Hyperparameters

Training Results

Analysis

DDQN Implementation

Algorithm Overview

Hyperparameters

Training Results

Analysis

Comparative Insights

Final Considerations

Future Work

Project Structure
sarsa_agent.py: SARSA agent implementation.

ddqn_agent.py: DDQN agent implementation.

main.py: Main training and evaluation script.

requirements.txt: Python package dependencies.

SARSA Implementation
Algorithm Overview
SARSA (State-Action-Reward-State-Action) is an on-policy RL algorithm that updates its Q-values based on the actions it actually takes, allowing the agent to continuously adapt its behavior as it interacts with the environment.

SARSA is particularly suitable for discrete, relatively simple environments like random attack simulations, where a compact state-action space allows for efficient Q-table management.

Hyperparameters
Learning Rate (α): 0.1

Discount Factor (γ): 0.99

Exploration Rate (ε): 0.1

Episodes: 1000

Training Results
Episode	Total Reward
0	3.60
100	21.66
200	30.56
300	6.46
400	10.21
500	5.16
600	9.54
700	10.24
800	9.99
900	6.17

Analysis
Initial Learning (Ep. 0–200): The agent improves its behavior over time, gradually increasing its average reward.

Fluctuations: The on-policy nature of SARSA causes reward variability due to ongoing exploration.

Stability: Although convergence is slow, the agent becomes increasingly effective in defending against random attacks.

DDQN Implementation
Algorithm Overview
Double Deep Q-Network (DDQN) is an off-policy deep reinforcement learning algorithm that uses two networks:

A Q-network for action selection

A target network for Q-value stabilization

DDQN reduces overestimation bias through double Q-learning and uses experience replay to improve sample efficiency.

Hyperparameters
Learning Rate (α): 0.001

Discount Factor (γ): 0.9

Exploration Rate (ε): 0.1

Batch Size: 64

Replay Memory: 10,000

Episodes: 1000

Training Results
Episode	Total Reward
0	39.10
100	5.14
200	1.43
300	30.68
400	8.84
500	5.68
600	3.48
700	6.17
800	6.40
900	10.99

Analysis
Stability: DDQN exhibits higher variance early in training but stabilizes with better rewards as learning progresses.

Effectiveness: Able to generalize well in both random and complex (maximal) attack settings.

Efficiency: Experience replay and separate target network lead to faster convergence compared to SARSA.

Comparative Insights
Feature	SARSA	DDQN
Learning Type	On-policy	Off-policy
Representation	Tabular	Neural Network
Exploration Strategy	ε-greedy	ε-greedy
Sample Efficiency	Low	High (via experience replay)
Stability	Moderate	Moderate to High (after warm-up)
Performance (Random)	Satisfactory	Good
Performance (Maximal)	Limited	Robust

Final Considerations
The results demonstrate that both SARSA and DDQN can effectively learn defensive behaviors in cyber environments, but they serve different roles:

SARSA performs well in simple, discrete scenarios like random attacks. It is computationally lightweight and easier to implement, but struggles with complex attack patterns or continuous state spaces.

DDQN, on the other hand, scales effectively to more complex environments like maximal attacks. Its use of deep learning enables generalization across larger and more varied state spaces, though it requires more computational resources and longer training times.

Key Takeaways
SARSA shows steady, interpretable progress, ideal for baseline evaluations or simple tasks.

DDQN offers superior adaptability and learning capacity, making it better suited for real-world or dynamic environments.

Both agents benefit from a careful balance between exploration and exploitation, controlled by the ε parameter.

Training reward plots indicate meaningful improvements for both agents, especially evident in the late training stages of DDQN.

Future Work
Integrate more advanced RL techniques like Proximal Policy Optimization (PPO) or Actor-Critic models.

Apply curriculum learning to improve early-stage convergence.

Simulate real-world threat models involving adaptive adversaries.

Implement online learning for continuous agent improvement in production environments.
