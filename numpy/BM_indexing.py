import google_benchmark as benchmark
import numpy as np


@benchmark.register
def BM_index_assign(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        sliced_mat[1, 2] = 5


@benchmark.register
def BM_index_get(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        sliced_mat[1, 2]


if __name__ == "__main__":
    benchmark.main()
