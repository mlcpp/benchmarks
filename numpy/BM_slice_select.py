import google_benchmark as benchmark
import numpy as np


@benchmark.register
def BM_slice_select(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    X = mat[1:5, :2]
    Y = mat[1:5, 2:3]
    while state:
        X[Y[:, 0] == 7.07]


if __name__ == "__main__":
    benchmark.main()
