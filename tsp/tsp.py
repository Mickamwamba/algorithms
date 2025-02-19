import random
from itertools import permutations
import matplotlib.pyplot as plt
import os
from datetime import datetime
from collections import Counter
# plt.ion()

parent_dir = os.path.abspath(os.path.join(os.getcwd(), "..","Algorithms"))
tsp_folder = os.path.join(parent_dir, "TSP")


def distance_tour(aTour):
    return sum(distance_points(aTour[i - 1], aTour[i]) for i in range(len(aTour)))


def distance_points(first,second): 
    return abs(first-second)

def generate_cities(number_of_cities):
    seed = 111; 
    width = 500
    height = 300 
    random.seed(number_of_cities,seed)
    return frozenset(aCity(random.randint(1, width), random.randint(1, height)) for c in range(number_of_cities))   
               

def brute_force(cities):
    "Generate all possible tours of the cities and choose the shortest tour."
    return shortest_tour(alltours(cities))

def shortest_tour(tours): 
    return min(tours, key=distance_tour)

def visualize_tour(tour, style='bo-'):

    # if len(tour) < 1000: 
    plt.figure(figsize=(15, 10))
    start = tour[0:1]
    visualize_segment(tour + start, style)
    visualize_segment(start, 'rD')

    # plt.savefig(os.path.join(os.path.abspath(os.path.join(os.getcwd(), "..")),"TSP","tour.png"))
    file_path = os.path.join(tsp_folder, "tour.png")
    # Save the plot
    plt.savefig(file_path)

    plt.show()


def visualize_segment (segment, style='bo-'):
    plt.plot([X(c) for c in segment], [Y(c) for c in segment], style, clip_on=False)
    plt.axis('scaled')
    plt.axis('off')

def X(city): 
    "X axis"; 
    return city.real
def Y(city):
    "Y axis"; 
    return city.imag


def tsp(algorithm,cities):
    t0 = datetime.now()
    tour = algorithm(cities)
    t1 = datetime.now()
    # Every city appears exactly once in tour
    assert Counter(tour) == Counter(cities)
    visualize_tour(tour)
    print("{}: {} cities => tour length {:.0f} (in {:.3f} sec)".format(name(algorithm), len(tour), distance_tour(tour), (t1 - t0).total_seconds()))

def name(algorithm): 
    return algorithm.__name__.replace('_tsp','')


def greedy_algorithm(cities,start=None):
    city_ = start or first(cities)
    tour = [city_]
    unvisited = set(cities-{city_})

    while(unvisited):
        city_ = nearest_neighbor(city_,unvisited)
        tour.append(city_)
        unvisited.remove(city_)

    return tour

def first(collection): 
    return next(iter(collection))

def nearest_neighbor(city_a,cities):
    return min(cities, key=lambda city_:distance_points(city_,city_a))


alltours = permutations
aCity = complex



# tsp(brute_force,generate_cities(10))
tsp(greedy_algorithm,generate_cities(2000))
