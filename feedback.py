from collections import Counter

def feedback(sigma, gamma):
    """
    Compute the Mastermind feedback score (black, white) for a guess gamma against the secret sigma.
    """
    black = 0  # exact matches (correct value and position)
    white = 0  # partial matches (correct value, wrong position)

    sigma_unmatched = []
    gamma_unmatched = []

    # Count black pegs (position-wise equality)
    for i in range(len(sigma)):
        if sigma[i] == gamma[i]:
            black += 1
        else:
            sigma_unmatched.append(sigma[i])
            gamma_unmatched.append(gamma[i])

    # Count white pegs by multiset intersection
    sigma_counter = Counter(sigma_unmatched)
    gamma_counter = Counter(gamma_unmatched)

    white = sum(min(gamma_counter[k], sigma_counter[k]) for k in gamma_counter)
    return (black, white)