import google_benchmark as benchmark
import numpy as np


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


if __name__ == "__main__":
    benchmark.main()
