🛡️ Cybersecurity for Healthcare Using Reinforcement Learning

🔍 Project Overview

This project explores how Reinforcement Learning (RL) can be applied to cyberattack defense strategies in healthcare systems. Two key algorithms are implemented and compared:

SARSA: A lightweight on-policy method

DDQN (Double Deep Q-Network): A more advanced, neural-network-based off-policy method

We simulate a healthcare cybersecurity environment using gym-idsgame, enabling the agents to learn and adapt to random and strategic attack scenarios.

⚙️ Technologies & Libraries
Python, Gym, PyTorch, Numpy, Matplotlib

Reinforcement Learning Algorithms: SARSA, DDQN

Environment: gym-idsgame (IDS simulation for cybersecurity)

🧠 Algorithms
✅ SARSA Agent
Approach: On-policy learning

Learning Rate (α): 0.1

Discount Factor (γ): 0.9

Exploration Rate (ε): 0.1

State Handling: Q-table based, with discretized observations

Use Case: Suitable for smaller, simpler environments

🤖 DDQN Agent
Approach: Off-policy with deep Q-learning

Architecture: Two neural networks (Q-network & Target network)

Replay Memory: Experience buffer of 10,000 transitions

Batch Size: 64

Optimization: Adam optimizer with MSE loss

Use Case: More stable in complex environments with larger state spaces

🏥 Scenario

Domain: Cyber defense in healthcare IT infrastructure

Simulation: Random attacks against a system with defense actions

Goal: Train agents to learn optimal defense strategies over time

📊 Training Outcomes
SARSA
Episode	Total Reward
0	~3.6
300	~11.8
900	~23.4

Trend: Gradual learning with improved performance

Behavior: Smooth convergence, sensitive to exploration rate

Strength: Stable learning, interpretable policy

DDQN
Episode	Total Reward
0	~39.1
300	~30.6
900	~10.9

Trend: High variance, initially strong but unstable

Behavior: Large reward swings; learning influenced by replay memory and delayed target updates

Strength: More suited for dynamic and high-dimensional attack environments

🔬 Key Insights

SARSA: Easier to train and understand, ideal for interpretable models in regulated environments like healthcare.

DDQN: More scalable and powerful, but requires careful tuning and longer training due to higher volatility.

🤝 Real-World Relevance

This simulation reflects how AI agents could defend healthcare systems against cyber threats through autonomous learning. Real-world applications include:

Intrusion Detection Systems (IDS)

Adaptive firewalls

Intelligent threat response automation

📈 Future Work
Introduce multi-agent settings for attack-defense dynamics

Extend to Zero-Day attack simulations

Integrate time-based or sequential attack vectors

Deploy agent via Streamlit or FastAPI for demo

📂 Project Structure
├── sarsa_agent.py       # SARSA implementation
├── ddqn_agent.py        # DDQN implementation
├── environment.py       # Custom Gym environment
├── train_sarsa.py       # SARSA training script
├── train_ddqn.py        # DDQN training script
├── plots/               # Training reward visualizations
└── README.md            # This file
