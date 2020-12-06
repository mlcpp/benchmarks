import google_benchmark as benchmark
import numpy as np


@benchmark.register
def BM_std_row(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        np.std(sliced_mat, 1)


@benchmark.register
def BM_std_column(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        np.std(sliced_mat, 0)


if __name__ == "__main__":
    benchmark.main()
