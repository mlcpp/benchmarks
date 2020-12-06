import google_benchmark as benchmark
import numpy as np


@benchmark.register
def BM_unary_minus(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        -sliced_mat


if __name__ == "__main__":
    benchmark.main()
