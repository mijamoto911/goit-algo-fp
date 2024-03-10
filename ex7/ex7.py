import random
from collections import Counter

def monte_carlo_simulation(num_simulations):
    results = Counter()

    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        total = dice1 + dice2

        results[total] += 1

    probabilities = {key: value / num_simulations * 100 for key, value in results.items()}

    return probabilities

def analytical_probabilities():
    probabilities = {}
    for total in range(2, 13):
        count = 0
        for dice1 in range(1, 7):
            for dice2 in range(1, 7):
                if dice1 + dice2 == total:
                    count += 1
        probabilities[total] = count / 36 * 100

    return probabilities

def display_results(monte_carlo_probabilities, analytical_probabilities):
    print("Sum\tMonte Carlo\tAnalytical calculation")
    for total in range(2, 13):
        print(f"{total}\t{monte_carlo_probabilities[total]:.2f}%\t\t{analytical_probabilities[total]:.2f}%")

if __name__ == "__main__":
    num_simulations = 1000000  

    monte_carlo_probabilities = monte_carlo_simulation(num_simulations)

    analytical_probabilities = analytical_probabilities()

    display_results(monte_carlo_probabilities, analytical_probabilities)
