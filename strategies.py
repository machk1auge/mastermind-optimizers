import random
from enum import Enum
from feedback import feedback
from minimax import minimax

# Define the code space for Mastermind (4 pegs, 6 colors)
CODE_SPACE = [[a, b, c, d] for a in range(6) for b in range(6) for c in range(6) for d in range(6)]

def bruteforce_strategy(sigma):
    """
    Brute-force strategy: iterates through all possible codes until the correct one is found.
    """
    for a in range(6):
        for b in range(6):
            for c in range(6):
                for d in range(6):
                    gamma = [a, b, c, d]
                    if feedback(sigma, gamma) == (4, 0):
                        return gamma

def random_strategy(sigma):
    """
    Random strategy: randomly selects a code until the correct one is found.
    """
    while True:
        gamma = [random.randint(0, 5) for _ in range(4)]
        if feedback(sigma, gamma) == (4, 0):
            return gamma

def knuth_random_strategy(sigma, initial_guess=[1, 1, 2, 2]):
    """
    Knuth's random strategy: uses Knuth's method to find the code, but selects guesses randomly.
    """

    S = CODE_SPACE.copy()
    gamma = initial_guess

    # Get initial feedback for the first guess
    score = feedback(sigma, gamma)

    while score != (4, 0):
        # Remove gamma from the candidate set scine it is not the solution
        S.remove(gamma)

        # Reduce S: keep only deltas where feedback(delta, gamma) == score
        # This ensures we only keep candidates that match the feedback of the last guess
        S = [delta for delta in S if feedback(delta, gamma) == score]

        # Randomly select the next guess from the remaining candidates
        gamma = random.choice(S)

        # Get feedback for the new guess
        score = feedback(sigma, gamma)

    return gamma

def knuth_minimax_strategy(sigma, initial_guess=[1, 1, 2, 2]):
    """
    Knuth's minimax strategy: uses Knuth's method to find the code, minimizing the maximum number of remaining candidates.
    """

    S = CODE_SPACE.copy()
    gamma = initial_guess
    score = feedback(sigma, gamma)

    while score != (4, 0):
        S.remove(gamma)
        S = [delta for delta in S if feedback(delta, gamma) == score]
        # Use minimax to select the next guess that minimizes the maximum number of remaining candidates
        gamma = minimax(S)
        score = feedback(sigma, gamma)

    return gamma

class Strategy(Enum):
    BRUTE_FORCE = bruteforce_strategy
    RANDOM = random_strategy
    KNUTH_RANDOM = knuth_random_strategy
    KNUTH_MINIMAX = knuth_minimax_strategy
