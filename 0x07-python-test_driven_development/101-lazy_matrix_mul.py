#!/usr/bin/python3
"""Defines a matrix multiplication using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the product of two matrices.
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
