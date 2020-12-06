import google_benchmark as benchmark
import numpy as np


@benchmark.register
def BM_zeros(state):
    while state:
        np.zeros((3, 4))


if __name__ == "__main__":
    benchmark.main()
