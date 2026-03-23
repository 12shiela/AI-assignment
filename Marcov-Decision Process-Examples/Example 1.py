import random

states = ["S0", "S1"]
actions = ["A0", "A1"]
transitions = {"S0":{"A0":"S1","A1":"S0"}, "S1":{"A0":"S0","A1":"S1"}}
rewards = {("S0","A0"):5, ("S0","A1"):1, ("S1","A0"):2, ("S1","A1"):3}
Q = {}
alpha, gamma = 0.1, 0.9
state = "S0"

for _ in range(100):
    action = random.choice(actions)
    next_state = transitions[state][action]
    reward = rewards[(state, action)]
    Q[(state, action)] = Q.get((state, action), 0) + alpha * (
        reward + gamma*max(Q.get((next_state,a),0) for a in actions) - Q.get((state, action),0)
    )
    state = next_state

print("Learned Q-values:", Q)