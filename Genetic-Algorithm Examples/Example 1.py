import random

def fitness(x): return x**2
population = [random.randint(-10, 10) for _ in range(10)]

for _ in range(30):
    scores = sorted(population, key=fitness, reverse=True)
    parents = scores[:2]
    child = (parents[0] + parents[1]) // 2
    if random.random() < 0.1: child += random.randint(-1, 1)
    population[-1] = child

print("Best solution:", max(population, key=fitness))