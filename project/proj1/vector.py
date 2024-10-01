from math import *
from typing import Union, List

vectype = List[Union[int, float]]


class Vector:
    def __init__(self, vector: vectype):
        if len(vector) == 0:
            raise ValueError("Vector must be non-empty")
        self.value = vector

    def __len__(self) -> int:
        """
        Operator to define vector dimension

        Returns
        -------
        int
            Vector dimension
        """
        return len(self.value)

    def __getitem__(self, key: int) -> Union[int, float]:
        """
        Operator for determining the key coordinate of a vector

        Returns
        -------
        Union[int, float]
            Key coordinate
        """
        return self.value[key]

    def scalar(self, v: "Vector") -> float:
        """
        Dot product function of vectors

        Parameters
        ----------
        v: vectype
            The vector to calculate the scalar product with

        Returns
        -------
        ans: float
            Dot product of given vectors
        """
        if len(self) != len(v):
            raise ValueError("Vectors size does not match")
        ans = 0.0
        for i in range(len(self.value)):
            ans += self[i] * v[i]
        return ans

    def norm(self) -> float:
        """
        Vector norm distribution function

        Returns
        -------
        ans: float
            Norm of a given vector
        """
        ans = 0.0
        for crd in self.value:
            ans += crd * crd
        return ans**0.5

    def angle(self, v: "Vector") -> float:
        """
        Function for calculating the angle between vectors

        Parameters
        ----------
        v: vectype
            The vector to calculate the angle

        Returns
        -------
        ans: float
            Angle between given vectors
        """
        if v.norm() == 0 or self.norm() == 0:
            return 0.0
        return acos(self.scalar(v) / (v.norm() * self.norm()))
