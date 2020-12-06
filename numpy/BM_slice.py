import google_benchmark as benchmark
import numpy as np


@benchmark.register
def BM_slice(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    while state:
        mat[1:, :]


if __name__ == "__main__":
    benchmark.main()
