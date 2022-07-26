import math
from I_II_portfolio_return import expret, expretport, var, varport


def main():
    correlations = [0.3, 1.0, -1.0]
    weight1 = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    weight2 = [(1-i) for i in weight1]
    return1=0.1
    return2=0.15
    sd1=0.16
    sd2=0.24
    print("Weight 1", "Weight 2", f"Mu{' '*6}", "Sigma")
    for correlation in correlations:
        for w1, w2 in zip(weight1, weight2):
            print(f"{w1}{' '*6}{w2:.1f}{' '*6}{w1*return1+w2*return2:.3f}{' '*4}"
                  f"{math.sqrt(w1**2*sd1**2+w2**2*sd2**2+2*w1*w2*sd1*sd2*correlation):.4f}")

if __name__ == "__main__":
    main()