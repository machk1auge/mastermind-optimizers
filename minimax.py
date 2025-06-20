from collections import Counter
from feedback import feedback

def minimax(candidates):
    """
    Minimax strategy: selects the guess that minimizes the maximum number of remaining candidates.
    """
    best_guess = None
    best_score = float('inf')

    for guess in candidates:
        # Partition counts by feedback
        partitions = Counter()
        for code in candidates:
            partitions[feedback(code, guess)] += 1

        # Find the biggest partition size. 
        # If max partition size is less than the best score found so far, update best_score and best_guess
        worst_case = max(partitions.values())
        if worst_case < best_score:
            best_score = worst_case
            best_guess = guess

    return best_guess