import numpy as np

def poisson_probability(lambda_, k):
    return (lambda_**k * np.exp(-lambda_)) / np.math.factorial(k)

def estimate_goal_probabilities(home_avg_goals, away_avg_goals, max_goals=5):
    home_probs = [poisson_probability(home_avg_goals, i) for i in range(max_goals + 1)]
    away_probs = [poisson_probability(away_avg_goals, i) for i in range(max_goals + 1)]

    over_1_5 = 0
    over_2_5 = 0
    btts = 0

    for i in range(max_goals + 1):
        for j in range(max_goals + 1):
            p = home_probs[i] * away_probs[j]
            if i + j > 1:
                over_1_5 += p
            if i + j > 2:
                over_2_5 += p
            if i > 0 and j > 0:
                btts += p

    return {
        "over_1_5": round(over_1_5 * 100, 2),
        "over_2_5": round(over_2_5 * 100, 2),
        "btts": round(btts * 100, 2)
    }
