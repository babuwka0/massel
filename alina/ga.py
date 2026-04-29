import random
import math
import matplotlib.pyplot as plt

POPULATION_SIZE = 20
GENES_COUNT = 100
MUTATION_RATE = 0.1
STOP_DISTANCE = 0.5

x_values = [i * 0.1 for i in range(GENES_COUNT)]
target_function = [math.sin(x) for x in x_values]

def create_individual():
    return [random.uniform(-1, 1) for _ in range(GENES_COUNT)]

def euclidean_distance(individual):
    distance = 0
    for i in range(GENES_COUNT):
        distance += (individual[i] - target_function[i]) ** 2
    return math.sqrt(distance)

def crossover(parent1, parent2):
    point = random.randint(1, GENES_COUNT - 1)
    return parent1[:point] + parent2[point:]

def mutate(individual):
    for i in range(GENES_COUNT):
        if random.random() < MUTATION_RATE:
            individual[i] += random.uniform(-0.1, 0.1)
    return individual

population = [create_individual() for _ in range(POPULATION_SIZE)]

generation = 0
best_distance = float("inf")
best_individual = None

print("генетический алгоритм запущен")
print("целевая функция: y = sin(x)")
print("--------------------------")

while best_distance > STOP_DISTANCE:
    generation += 1

    scored_population = []
    for individual in population:
        scored_population.append((euclidean_distance(individual), individual))

    scored_population.sort(key=lambda x: x[0])

    best_distance = scored_population[0][0]
    best_individual = scored_population[0][1]

    print(f"поколение {generation}, лучшее расстояние = {best_distance:.4f}")

    survivors = [ind for (_, ind) in scored_population[:POPULATION_SIZE]]

    new_population = survivors.copy()
    while len(new_population) < POPULATION_SIZE * 2:
        parent1 = random.choice(survivors)
        parent2 = random.choice(survivors)
        child = mutate(crossover(parent1, parent2))
        new_population.append(child)

    scored_new_population = []
    for individual in new_population:
        scored_new_population.append((euclidean_distance(individual), individual))

    scored_new_population.sort(key=lambda x: x[0])
    population = [ind for (_, ind) in scored_new_population[:POPULATION_SIZE]]

print("--------------------------")
print("условие остановки достигнуто")
print(f"итоговое расстояние: {best_distance:.4f}")

plt.figure(figsize=(10, 5))
plt.plot(x_values, target_function, label="y = sin(x)", linewidth=2)
plt.plot(x_values, best_individual, label="лучшая особь", linestyle="--")
plt.legend()
plt.title("результат работы генетического алгоритма")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
