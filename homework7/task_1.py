class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, x)) for x in self.matrix])
        # for i in self.matrix:
        #     print(' '.join(list(map(str, i))))
        # return str()

    def __add__(self, other):
        result = [map(sum, zip(*i)) for i in zip(self.matrix, other.matrix)]
        return Matrix(result)


m = Matrix([[3, 2, 1], [5, 8, 9], [4, 8, 9]])
n = Matrix([[5, 8, 0], [5, 2, 1], [2, 9, 7]])
tilt = m + n
print(tilt)
# print(m)
