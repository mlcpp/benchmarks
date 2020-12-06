import google_benchmark as benchmark
import numpy as np


@benchmark.register
def BM_element_wise_multiplication_mat_mat(state):
    mat1 = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    mat2 = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat1 = mat1[1:, :]
    sliced_mat2 = mat2[1:, :]
    while state:
        sliced_mat1*sliced_mat2


@benchmark.register
def BM_element_wise_multiplication_mat_sca(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        sliced_mat*2


@benchmark.register
def BM_element_wise_multiplication_mat_vec(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        sliced_mat*sliced_mat[1:2, 0:]


if __name__ == "__main__":
    benchmark.main()
