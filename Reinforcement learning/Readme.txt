🛡️ Cybersecurity for Healthcare using Reinforcement Learning

A Simulation Framework with SARSA and DDQN in IDS Environments
This project explores the application of Reinforcement Learning (RL) for simulating and improving cyber defense strategies in sensitive environments like healthcare infrastructure. It leverages the gym-idsgame environment to model intrusion scenarios and trains RL agents (SARSA & DDQN) to learn defensive behaviors against random and maximal cyber attacks.

🎯 Objective

To evaluate and compare two reinforcement learning techniques — SARSA (on-policy tabular learning) and DDQN (deep off-policy learning) — for their ability to learn and adapt to unpredictable cyber attacks within a controlled intrusion detection simulation.

🧠 Technologies Used

Component	Description
gym-idsgame	Simulates attacker-defender environments for RL training
SARSA Agent	Tabular, on-policy agent for early-stage defense learning
DDQN Agent	Deep Q-Learning agent with target networks and replay
PyTorch	Used to implement and train neural networks for DDQN
Matplotlib	Visualizes training reward evolution over episodes

💼 Business Relevance

Cybersecurity in healthcare is a high-stakes environment where even a few minutes of downtime can cost lives.

✅ This project simulates how adaptive, self-learning defense systems can mitigate threats where static rule-based systems fall short.

Key Business Outcomes:

🧬 Healthcare Relevance: Simulates attack-defense in settings with sensitive data (e.g., patient records, connected medical devices)

🔄 Adaptivity: RL agents learn to adapt to changing threat patterns

💸 Cost Efficiency: Reduces reliance on rule-based updates & manual monitoring

🔐 Resilience Simulation: Helps model breach-resistance of future network architectures

🧪 Use Case Scenarios

🏥 Hospital Network Simulation: Test IDS policy learning against adversarial behavior

🧑‍⚕️ Medical IoT Defense: Model attacks on connected devices and adjust defenses

📊 Security Policy Optimization: Use agent performance to tune resource allocation

📉 Incident Response Simulation: Use RL reward drops to model threat detection timing

📈 Performance Overview

Metric	SARSA Agent	DDQN Agent
Max Reward Achieved (Ep. 900)	23.42	39.10
Stability over Episodes	Medium	Low (initially)
Learning Curve	Steady Growth	Volatile, then rise
Best Use Case	Simple attack patterns	Complex evolving threats

🔍 Insight: DDQN's deep learning and replay memory enable long-term learning, while SARSA offers faster stability in simpler threat landscapes.

🔁 Agent Comparison

✅ SARSA:
Pros: Simple, stable, lower resource use

Cons: Limited scalability in large/complex environments

✅ DDQN:
Pros: Scalable, adaptable, better long-term results

Cons: Slower to stabilize, sensitive to hyperparameters

⚙️ How to Run

# Clone the environment
git clone https://github.com/Limmen/gym-idsgame
cd gym-idsgame
pip install -e .

# Install dependencies
pip install gym-idsgame scikit-learn torch matplotlib

# Run SARSA agent
python sarsa_agent.py

# Run DDQN agent
python ddqn_agent.py

📁 Project Structure

📦 cyber-rl-healthcare/
├── sarsa_agent.py           # SARSA implementation
├── ddqn_agent.py            # DDQN implementation
├── results/                 # Plots and reward evolution
├── README.md                # Project overview
└── requirements.txt         # Dependencies

📊 Future Enhancements

Area	Roadmap
Environment	Add real-world intrusion data or simulated hospital topologies
Evaluation	Integrate precision/recall of anomaly detection
Visualization	Heatmaps of decision space and Q-table evolution
Explainability	Add SHAP-like interpretation for DDQN neural weights
Deployment	Wrap agents into a REST API for real-time inference

📌 Key Learnings
RL methods like SARSA can quickly stabilize but plateau early.

DDQN offers greater capacity to handle noise and complexity but requires longer training.

Even simple environments reveal critical dynamics between exploration, exploitation, and policy stability in cyber defense.

