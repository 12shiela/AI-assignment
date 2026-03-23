import random

states = [(x,y) for x in range(2) for y in range(2)]
actions = ["UP","DOWN","LEFT","RIGHT"]
rewards = {((1,1),a):10 for a in actions}  # goal state
Q = {}
alpha, gamma = 0.1, 0.9
state = (0,0)

def next_state(s,a):
    x,y = s
    if a=="UP": return (x,min(1,y+1))
    if a=="DOWN": return (x,max(0,y-1))
    if a=="LEFT": return (max(0,x-1),y)
    if a=="RIGHT": return (min(1,x+1),y)
    return s

for _ in range(200):
    action = random.choice(actions)
    ns = next_state(state, action)
    reward = rewards.get((state, action), -1)
    Q[(state, action)] = Q.get((state, action),0) + alpha * (
        reward + gamma*max(Q.get((ns,a),0) for a in actions) - Q.get((state, action),0)
    )
    state = ns

print("Learned Q-values:", Q)