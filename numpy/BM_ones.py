import google_benchmark as benchmark
import numpy as np


@benchmark.register
def BM_ones(state):
    while state:
        np.ones((3, 4))


if __name__ == "__main__":
    benchmark.main()
