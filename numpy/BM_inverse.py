import google_benchmark as benchmark
import numpy as np


@benchmark.register
def BM_inverse(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    sq_mat = mat[1:4, 0:3]
    while state:
        np.linalg.inv(sq_mat)


if __name__ == "__main__":
    benchmark.main()
