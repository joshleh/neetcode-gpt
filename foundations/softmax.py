import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        denominator = 0
        probabilities = []

        for i in range(len(z)):
            denominator += np.e ** (z[i] - max(z))
            
        for i in range(len(z)):
            numerator = np.e ** (z[i] - max(z))
            prob = numerator / denominator
            probabilities.append(np.round(prob, 4))

        return probabilities
