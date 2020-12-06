import google_benchmark as benchmark
import numpy as np


@benchmark.register
def BM_genfromtxt(state):
    while state:
        np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')


if __name__ == "__main__":
    benchmark.main()
