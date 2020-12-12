import numpy as np

def invertX(matrix): 
    return np.linalg.inv(matrix)

def computeB(invertedMatrix, xy):
    return np.dot(invertedMatrix, xy)

def main():
    x = np.array([[10, 30, 40],
                  [30, 92, 119],
                  [40, 119, 163]])
    xy = ([[20],
           [59],
           [88]])
    b = computeB(invertX(x), xy)
    print(b)

if __name__ == "__main__":
    main()