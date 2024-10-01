import pytest


from project.proj1.vector import Vector
from math import *


@pytest.mark.parametrize(
    "v1, v2, res",
    [
        ([0.25, 1, 3], [-7, 2, -4], -11.75),
        ([2, -0.235, 6], [0.512, -0.234, 8], 49.07899),
        ([-1, -0.2, 0.8], [5, 2.9, 4.3], -2.14),
    ],
)
def test_scalar(v1, v2, res):
    v1, v2 = Vector(v1), Vector(v2)
    assert Vector.scalar(v1, v2) == res


@pytest.mark.parametrize(
    "v, res",
    [
        ([3, -5, 12], 178**0.5),
        ([-2, -1, -1], 6**0.5),
        ([5, 7, 2.512], 0.008 * (1254846**0.5)),
    ],
)
def test_norm(v, res):
    v = Vector(v)
    assert v.norm() == res


@pytest.mark.parametrize(
    "v1, v2, res",
    [
        ([1, 2, 3], [-3, -2, 7], acos((217**0.5) / 31)),
        ([-2, -3, 4], [6, -5, 1], acos(7 / (1798**0.5))),
        ([1, -2, 5, -3], [-3, 9, 2, 1], acos(-14 / (3705**0.5))),
    ],
)
def test_angle(v1, v2, res):
    v1, v2 = Vector(v1), Vector(v2)
    assert Vector.angle(v1, v2) == res
