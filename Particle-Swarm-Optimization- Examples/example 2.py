import random

def objective(x, y): return x**2 + y**2
particles = [(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(10)]
velocities = [(0,0)]*10
personal_best = particles[:]
global_best = min(particles, key=lambda p: objective(*p))

for _ in range(50):
    for i in range(len(particles)):
        r1, r2 = random.random(), random.random()
        vx = (0.5*velocities[i][0] +
              1.5*r1*(personal_best[i][0]-particles[i][0]) +
              1.5*r2*(global_best[0]-particles[i][0]))
        vy = (0.5*velocities[i][1] +
              1.5*r1*(personal_best[i][1]-particles[i][1]) +
              1.5*r2*(global_best[1]-particles[i][1]))
        velocities[i] = (vx, vy)
        particles[i] = (particles[i][0]+vx, particles[i][1]+vy)
        if objective(*particles[i]) < objective(*personal_best[i]):
            personal_best[i] = particles[i]
    global_best = min(personal_best, key=lambda p: objective(*p))

print("Best solution:", global_best)