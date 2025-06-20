from strategies import Strategy

def run_all_strategies(sigma):
    """
    Run all strategies on the given secret code sigma.
    """

    strategies = [
        Strategy.BRUTE_FORCE,
        Strategy.RANDOM,
        Strategy.KNUTH_RANDOM,
        Strategy.KNUTH_MINIMAX
    ]
    
    results = {}
    
    for strategy in strategies:
        result = strategy(sigma)
        results[strategy] = result
    
    return results

def main():
    sigma = [1, 2, 3, 4]
    results = run_all_strategies(sigma)
    for strategy_name, result in results.items():
        print(f"{strategy_name}: {result}")

if __name__ == "__main__":
    main()