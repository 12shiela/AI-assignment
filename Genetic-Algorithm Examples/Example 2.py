import random

target = "HELLO"
population = ["".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(len(target))) for _ in range(20)]

def fitness(s): return sum(1 for a, b in zip(s, target) if a == b)

for _ in range(100):
    population.sort(key=fitness, reverse=True)
    parents = population[:2]
    child = "".join(random.choice([parents[0][i], parents[1][i]]) for i in range(len(target)))
    if random.random() < 0.2:
        idx = random.randint(0, len(target)-1)
        child = child[:idx] + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + child[idx+1:]
    population[-1] = child

print("Best solution:", max(population, key=fitness))