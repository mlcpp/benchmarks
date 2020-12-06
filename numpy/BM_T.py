import google_benchmark as benchmark
import numpy as np


@benchmark.register
def BM_T(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    while state:
        mat.T


if __name__ == "__main__":
    benchmark.main()
