import numpy as np

def flip(part:np.ndarray, axis:str) -> np.ndarray:
    size = part.shape
    flipped = np.zeros_like(part)
    if axis == 'x':
        size = size[0]
        iterator = int(size/2)
        for i in range(iterator):
            flipped[i, :], flipped[size - 1 - i, :] = part[size - 1 - i, :], part[i, :]
            pass
    elif axis == 'y':
        size = size[1]
        iterator = int(size/2)
        for i in range(iterator):
            flipped[:, i], flipped[:, size - 1 - i] = part[:, size - 1 - i], part[:, i]
            pass
    else:
        return None
    return flipped

def horizontal():
    pass