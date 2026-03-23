import random

def objective(x): return x**2
particles = [random.uniform(-10, 10) for _ in range(10)]
velocities = [0]*10
personal_best = particles[:]
global_best = min(particles, key=objective)

for _ in range(50):
    for i in range(len(particles)):
        r1, r2 = random.random(), random.random()
        velocities[i] = (0.5*velocities[i] +
                         1.5*r1*(personal_best[i]-particles[i]) +
                         1.5*r2*(global_best-particles[i]))
        particles[i] += velocities[i]
        if objective(particles[i]) < objective(personal_best[i]):
            personal_best[i] = particles[i]
    global_best = min(personal_best, key=objective)

print("Best solution:", global_best)