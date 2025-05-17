#!/usr/bin/python3
"""
101-lazy_matrix_mul.py
Function that multiplies 2 matrices by using the module NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy.

    Args:
        m_a: First matrix (list of lists of integers/floats)
        m_b: Second matrix (list of lists of integers/floats)

    Returns:
        The resulting matrix as a NumPy array

    Raises:
        TypeError: If matrices are not lists of lists, or contain invalid types
        ValueError: If matrices are empty or can't be multiplied
    """
    err_msg = {
        'm_a_not_list': "m_a must be a list",
        'm_b_not_list': "m_b must be a list",
        'm_a_not_list_of_lists': "m_a must be a list of lists",
        'm_b_not_list_of_lists': "m_b must be a list of lists",
        'm_a_empty': "m_a can't be empty",
        'm_b_empty': "m_b can't be empty",
        'm_a_invalid_type': "m_a should contain only integers or floats",
        'm_b_invalid_type': "m_b should contain only integers or floats",
        'm_a_uneven_rows': "each row of m_a must be of the same size",
        'm_b_uneven_rows': "each row of m_b must be of the same size",
        'cant_multiply': "m_a and m_b can't be multiplied"
    }

    if type(m_a) != list:
        raise TypeError(err_msg['m_a_not_list'])

    if any(type(row) != list for row in m_a):
        raise TypeError(err_msg['m_a_not_list_of_lists'])

    if type(m_b) != list:
        raise TypeError(err_msg['m_b_not_list'])

    if any(type(row) != list for row in m_b):
        raise TypeError(err_msg['m_b_not_list_of_lists'])

    if m_a == [] or m_a == [[]]:
        raise ValueError(err_msg['m_a_empty'])

    if m_b == [] or m_b == [[]]:
        raise ValueError(err_msg['m_b_empty'])

    for row in m_a:
        for element in row:
            if type(element) not in (int, float):
                raise TypeError(err_msg['m_a_invalid_type'])

    for row in m_b:
        for element in row:
            if type(element) not in (int, float):
                raise TypeError(err_msg['m_b_invalid_type'])

    if any(len(m_a[0]) != len(row) for row in m_a):
        raise TypeError(err_msg['m_a_uneven_rows'])

    if any(len(m_b[0]) != len(row) for row in m_b):
        raise TypeError(err_msg['m_b_uneven_rows'])

    if len(m_a[0]) != len(m_b):
        raise ValueError(err_msg['cant_multiply'])

    return np.matmul(m_a, m_b)
