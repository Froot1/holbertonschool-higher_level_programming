#!/usr/bin/python3
"""
lazy matrix math
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """calculates multiplication"""
    return np.dot(m_a, m_b)
