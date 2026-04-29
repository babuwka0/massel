import math
import random

import matplotlib.pyplot as plt


POPULATION_SIZE = 20
GENES_COUNT = 100
MUTATION_RATE = 0.1
STOP_DISTANCE = 0.5

#контроль рандома
random.seed(22)

#вариант22: y= ln(4x).

x_values = [round((i + 1) * 0.1, 1) for i in range(GENES_COUNT)]
target_function = [math.log(4 * x) for x in x_values]

min_y = min(target_function)
max_y = max(target_function)


def create_individual():
    return [random.uniform(min_y - 1, max_y + 1) for _ in range(GENES_COUNT)]

def euclidean_distance(individual):
    distance = 0
    for i in range(GENES_COUNT):
        distance += (individual[i] - target_function[i]) ** 2
    return math.sqrt(distance)

def crossover(parent1, parent2):
    child = []
    for i in range(GENES_COUNT):
        if random.random() < 0.5:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return child

#def mutate(individual, generation):
def mutate(individual):
    #mutation_power = max(0.02, 0.5 / (1 + generation / 500))
    mutation_power = 0.1
    for i in range(GENES_COUNT):
        if random.random() < MUTATION_RATE:
            individual[i] += random.uniform(-mutation_power, mutation_power)
    return individual

def select_best(population):
    scored_population = []
    for individual in population:
        scored_population.append((euclidean_distance(individual), individual))
    scored_population.sort(key=lambda item: item[0])
    return scored_population[:POPULATION_SIZE]

def run_genetic_algorithm():
    population = [create_individual() for _ in range(POPULATION_SIZE)]
    generation = 0
    best_distance = float("inf")
    best_individual = None

    print("Генетический алгоритм запущен")
    print("Вариант 22: y = ln(4x)")
    print("Интервал: [0.1; 10.0], шаг = 0.1")
    print("-" * 40)

    while best_distance > STOP_DISTANCE:
        generation += 1

        scored_population = select_best(population)
        best_distance = scored_population[0][0]
        best_individual = scored_population[0][1]

        if generation == 1 or generation % 100 == 0 or best_distance <= STOP_DISTANCE:
            print(f"Поколение {generation} лучшее расстояние = {best_distance:.4f}")

        survivors = [individual for _, individual in scored_population]
        new_population = survivors.copy()

        while len(new_population) < POPULATION_SIZE * 2:
            parent1 = random.choice(survivors)
            parent2 = random.choice(survivors)
            child = crossover(parent1, parent2)
            child = mutate(child)
            #child = mutate(child, generation)
            new_population.append(child)

        population = [individual for _, individual in select_best(new_population)]

    print("-" * 40)
    print("Условие остановки достигнуто")
    print(f"Итоговое поколение: {generation}")
    print(f"Итоговое расстояние: {best_distance:.4f}")

    return best_individual, best_distance, generation


best_individual, best_distance, generation = run_genetic_algorithm()

plt.figure(figsize=(10, 5))
plt.plot(x_values, target_function, label="y = ln(4x)", linewidth=2)
plt.plot(x_values, best_individual, label="лучшая особь", linestyle="--")
plt.title("Результат работы генетического алгоритма для y = ln(4x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.savefig("result_ln4x.png", dpi=300, bbox_inches="tight")
plt.show()
