import random

# Функция приспособленности
def fitnessFunction(x, y):
    return 1 / (1 + x**2 + y**2)

# Генерация случайной популяции
def generatePopulation(size, xRange, yRange):
    population = []
    for _ in range(size):
        x = random.uniform(xRange[0], xRange[1])
        y = random.uniform(yRange[0], yRange[1])
        population.append((x, y))
    return population

# Оценка популяции
def evaluatePopulation(population):
    return [(ind, fitnessFunction(ind[0], ind[1])) for ind in population]

# Отбор (турнирный отбор)
def select(population, tournamentSize):
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(population, tournamentSize)
        winner = max(tournament, key=lambda ind: ind[1])
        selected.append(winner[0])
    return selected

# Рекомбинация (одноточечное скрещивание)
def recombine(parent1, parent2):
    alpha = random.random()
    child1 = (alpha * parent1[0] + (1 - alpha) * parent2[0], alpha * parent1[1] + (1 - alpha) * parent2[1])
    child2 = ((1 - alpha) * parent1[0] + alpha * parent2[0], (1 - alpha) * parent1[1] + alpha * parent2[1])
    return child1, child2

# Мутация
def mutate(individual, mutationRate, xRange, yRange):
    x, y = individual
    if random.random() < mutationRate:
        x = random.uniform(xRange[0], xRange[1])
    if random.random() < mutationRate:
        y = random.uniform(yRange[0], yRange[1])
    return (x, y)

# Генетический алгоритм
def geneticAlgorithm(popSize, generations, xRange, yRange, tournamentSize, mutationRate):
    population = generatePopulation(popSize, xRange, yRange)
    for generation in range(generations):
        evaluatedPopulation = evaluatePopulation(population)
        selectedPopulation = select(evaluatedPopulation, tournamentSize)
        newPopulation = []
        for i in range(0, len(selectedPopulation), 2):
            parent1 = selectedPopulation[i]
            parent2 = selectedPopulation[i + 1]
            child1, child2 = recombine(parent1, parent2)
            child1 = mutate(child1, mutationRate, xRange, yRange)
            child2 = mutate(child2, mutationRate, xRange, yRange)
            newPopulation.extend([child1, child2])
        population = newPopulation
        bestIndividual = max(evaluatedPopulation, key=lambda ind: ind[1])
        print(f"Generation {generation}: Best Individual = {bestIndividual[0]}, Fitness = {bestIndividual[1]}")
    return bestIndividual

# Параметры генетического алгоритма
popSize = 100
generations = 50
xRange = (-10, 10)
yRange = (-10, 10)
tournamentSize = 5
mutationRate = 0.01

# Запуск генетического алгоритма
bestSolution = geneticAlgorithm(popSize, generations, xRange, yRange, tournamentSize, mutationRate)
print(f"Best Solution: {bestSolution}")