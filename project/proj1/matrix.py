from typing import List, Union


mtype = List[List[Union[int, float]]]


class Matrix:
    def __init__(self, values: mtype):
        self.value = values
        if len(values) == 0 or len(values[0]) == 0:
            raise ValueError("The entered matrix is icorrect")
        for x in values:
            if len(x) != len(values[0]):
                raise ValueError("The entered matrix is icorrect")

    def __add__(self, other: "Matrix") -> "Matrix":
        """
        Addition operator for matrices

        Parameters
        ----------
        other: mtype
            Matrix with which to add the current matrix

        Returns
        -------
        mtype
            Result from the addition
        """
        if len(self) != len(other) or len(self[0]) != len(other[0]):
            raise ValueError("The dimensions of the matrices must be the same")
        return Matrix(
            [
                [self[i][j] + other[i][j] for j in range(len(self[0]))]
                for i in range(len(self))
            ]
        )

    def __getitem__(self, key: int) -> List[Union[int, float]]:
        """
        An indexing operator for accessing matrix elements

        Parameters
        ----------
        key: int
            Index of the matrix row to be retrieved

        Returns
        -------
        List[Union[int, float]]
            List of matrix row elements corresponding to the specified index

        """
        return self.value[key]

    def __iter__(self):
        return (x for x in self.value)

    def __len__(self):
        """
        Operator for determining the length of a matrix

        Returns:
            int: Number of rows in the matrix
        """
        return len(self.value)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Matrix):
            return NotImplemented
        return self.value == other.value

    def __matmul__(self, other: "Matrix") -> "Matrix":
        """
        Multiplies a matrix by another matrix

        Parameters
        ----------
        other: Matrix
            The matrix to multiply with

        Returns
        -------
        res: Matrix
            The product of two matrices
        """
        l, n, m = len(self), len(other[0]), len(other)
        if len(self[0]) != m:
            raise ValueError("Matrices of this dimensions cannot be multiplied")
        res = [[0.0 for _ in range(n)] for _ in range(l)]
        for i in range(l):
            for j in range(n):
                for r in range(m):
                    res[i][j] += self[i][r] * other[r][j]
        return Matrix([[x for x in row] for row in res])

    def __str__(self):
        return str(self.value)

    def transpose(self) -> "Matrix":
        """
        Transposes the matrix

        Returns
        -------
        matrix: Matrix
            Transposing of given matrix
        """
        if len(self) != len(self[0]):
            raise ValueError("Matrix is to be quadratic")
        return Matrix([[x[i] for x in self] for i in range(len(self))])
