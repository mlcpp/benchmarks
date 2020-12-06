import google_benchmark as benchmark
import numpy as np


@benchmark.register
def BM_eye(state):
    while state:
        np.eye(4)


if __name__ == "__main__":
    benchmark.main()
