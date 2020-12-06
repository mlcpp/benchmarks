import google_benchmark as benchmark
import numpy as np


@benchmark.register
def BM_abs(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]

    sliced_mat = -sliced_mat
    while state:
        np.abs(sliced_mat)


if __name__ == "__main__":
    benchmark.main()
