import google_benchmark as benchmark
import numpy as np


@benchmark.register
def BM_power_mat_mat(state):
    mat1 = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    mat2 = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat1 = mat1[1:, :]
    sliced_mat2 = mat2[1:, :]
    while state:
        np.power(sliced_mat1, sliced_mat2)


@benchmark.register
def BM_power_mat_sca(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        np.power(sliced_mat, 2)


if __name__ == "__main__":
    benchmark.main()
