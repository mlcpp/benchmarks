import google_benchmark as benchmark
import numpy as np


@benchmark.register
def BM_matmul(state):
    mat = np.genfromtxt("./datasets/boston/boston.csv", delimiter=',')
    mat1 = mat[1:5, :2]
    mat2 = mat[7:9, :3]
    while state:
        mat1@mat2


if __name__ == "__main__":
    benchmark.main()
