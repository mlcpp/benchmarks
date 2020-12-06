import google_benchmark as benchmark
import numpy as np


@benchmark.register
def BM_mean_row(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        np.mean(sliced_mat, 1)


@benchmark.register
def BM_mean_column(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        np.mean(sliced_mat, 0)


if __name__ == "__main__":
    benchmark.main()
