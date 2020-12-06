import google_benchmark as benchmark
import numpy as np


@benchmark.register
def BM_abs(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]

    sliced_mat = -sliced_mat
    while state:
        np.abs(sliced_mat)


@benchmark.register
def BM_addition_mat_mat(state):
    mat1 = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    mat2 = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat1 = mat1[1:, :]
    sliced_mat2 = mat2[1:, :]
    while state:
        sliced_mat1+sliced_mat2


@benchmark.register
def BM_addition_mat_sca(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        sliced_mat+1


@benchmark.register
def BM_addition_mat_vec(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        sliced_mat+sliced_mat[1:2, 0:]


@benchmark.register
def BM_argmax_row(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        np.argmax(sliced_mat, 1)


@benchmark.register
def BM_argmax_column(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        np.argmax(sliced_mat, 0)


@benchmark.register
def BM_argmin_row(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        np.argmin(sliced_mat, 1)


@benchmark.register
def BM_argmin_column(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        np.argmin(sliced_mat, 0)


@benchmark.register
def BM_concatenate_row(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    matr1_5 = mat[1:5, :]
    matr7_9 = mat[7:9, :]
    while state:
        np.concatenate((matr1_5, matr7_9), 0)


@benchmark.register
def BM_concatenate_column(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    matc0_3 = mat[1:10, :3]
    matc5_9 = mat[1:10, 5:9]
    while state:
        np.concatenate((matc0_3, matc5_9), 1)


@benchmark.register
def BM_delete_row(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    while state:
        np.delete(mat, 2, 0)


@benchmark.register
def BM_delete_column(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    while state:
        np.delete(mat, 1, 1)


@benchmark.register
def BM_determinant(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sq_mat = mat[1:4, 0:3]
    while state:
        np.linalg.det(sq_mat)


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


@benchmark.register
def BM_exp(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        np.exp(sliced_mat)


@benchmark.register
def BM_eye(state):
    while state:
        np.eye(4)


@benchmark.register
def BM_genfromtxt(state):
    while state:
        np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')


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


@benchmark.register
def BM_inverse(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sq_mat = mat[1:4, 0:3]
    while state:
        np.linalg.inv(sq_mat)


@benchmark.register
def BM_log(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        np.log(sliced_mat)


@benchmark.register
def BM_matmul(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    mat1 = mat[1:5, :2]
    mat2 = mat[7:9, :3]
    while state:
        mat1@mat2


@benchmark.register
def BM_max_row(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        np.max(sliced_mat, 1)


@benchmark.register
def BM_max_column(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        np.max(sliced_mat, 0)


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


@benchmark.register
def BM_min_row(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        np.min(sliced_mat, 1)


@benchmark.register
def BM_min_column(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        np.min(sliced_mat, 0)


@benchmark.register
def BM_ones(state):
    while state:
        np.ones((3, 4))


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


@benchmark.register
def BM_reciprocal(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        1/sliced_mat


@benchmark.register
def BM_slice_select(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    X = mat[1:5, :2]
    Y = mat[1:5, 2:3]
    while state:
        X[Y[:, 0] == 7.07]


@benchmark.register
def BM_slice(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    while state:
        mat[1:, :]


@benchmark.register
def BM_sqrt(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        np.sqrt(sliced_mat)


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


@benchmark.register
def BM_sum_row(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        np.sum(sliced_mat, 1)


@benchmark.register
def BM_sum_column(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        np.sum(sliced_mat, 0)


@benchmark.register
def BM_T(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    while state:
        mat.T


@benchmark.register
def BM_unary_minus(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sliced_mat = mat[1:, :]
    while state:
        -sliced_mat


@benchmark.register
def BM_zeros(state):
    while state:
        np.zeros((3, 4))


if __name__ == "__main__":
    benchmark.main()
