# 1.2 Suppose that there are two investments with the same probability distribution of returns as in Problem 1.1.The
# correlation between the returns is 0.15.What is the expected return and standard deviation of return from a
# portfolio where money is divided equally between the investments?
from math import sqrt




def expret(prob, ret):
    """return expected return given probability of different returns. Returns should be in decimal format e.g. 0.4"""

    return sum([i * j for i, j in zip(prob, ret)])


def expretport(w1, w2, prob1, ret1, prob2, ret2):
    """return expected return of portfolio of two assets given weights w1 and w2"""

    return w1 * expret(prob1, ret1) + w2 * expret(prob2, ret2)


def var(prob, ret):
    expectedreturn = expret(prob, ret)
    return sum([i * abs(j - expectedreturn) ** 2 for i, j in zip(prob, ret)])


def varport(w1, w2, prob1, ret1, prob2, ret2, corr):
    var1 = var(prob1, ret1)
    var2 = var(prob2, ret2)
    sd1 = sqrt(var1)
    sd2 = sqrt(var2)
    return sqrt(w1 ** 2 * var1 + w2 ** 2 * var2 + 2 * w1 * w2 * sd1 * sd2 * corr)


def main():
    probabilities = [0.1, 0.2, 0.35, 0.25, 0.1]
    returns = [40, 30, 15, -5, -15]
    correlation = 0.15

    weight1 = 0.5
    weight2 = 0.5

    returns = [i / 100 for i in returns]

    print(f"{expretport(weight1, weight2, probabilities, returns, probabilities, returns):.3f}")
    print(f"{varport(weight1, weight2, probabilities, returns, probabilities, returns, correlation):.4f}")

if __name__=="__main__":
    main()