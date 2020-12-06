import google_benchmark as benchmark
import numpy as np


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


if __name__ == "__main__":
    benchmark.main()
