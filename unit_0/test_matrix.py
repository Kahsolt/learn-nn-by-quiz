import torch
from torch import Tensor


def is_matrix(A:Tensor) -> bool:
    # TODO: 判断张量 A 是不是个矩阵

    return False


def is_square(A:Tensor) -> bool:
    # TODO: 判断矩阵 A 是不是个方阵

    return False


def get_trace(A:Tensor) -> float:
    # TODO: 计算矩阵 A 的迹

    return 0.0


def is_commutative(A:Tensor, B:Tensor) -> bool:
    # TODO: 判断矩阵 A 和 B 是否可交换，即 dot(A, B) == dot(B, A)

    return False


if __name__ == '__main__':
    assert not is_matrix(Tensor([]))
    assert not is_matrix(Tensor([1.]))
    assert not is_matrix(Tensor([1., 2.]))
    assert not is_matrix(Tensor([[1.]]))
    assert is_matrix(Tensor([[1., 2.]]))
    assert is_matrix(Tensor([[1., 2.], [3, 4]]))
    assert not is_matrix(Tensor([[[1., 2.], [3, 4]]]))


    assert is_square(Tensor([[1.]]))
    assert not is_square(Tensor([[[1., 2.]]]))
    assert is_square(Tensor([[[1., 2.], [3, 4]]]))


    A = Tensor([
        [4, -1]
        [7, 6],
    ])
    assert 10 - get_trace(A) < 1e-5

    A = Tensor([
        [-7, 4]
        [0, 5],
    ])
    assert -2 - get_trace(A) < 1e-5


    A = Tensor([
        [1, 1],
        [0, 1],
    ])
    B = Tensor([
        [0, 0],
        [-1, 0]
    ])
    assert is_commutative(A, B)

    B = Tensor([
        [1, 0],
        [-1, 0]
    ])
    assert not is_commutative(A, B)
