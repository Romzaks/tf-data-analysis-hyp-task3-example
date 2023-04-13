import pandas as pd
import numpy as np
from scipy.stats import pearsonr

chat_id = 333357078 # Ваш chat ID, не меняйте название переменной

def statistic(x, y):
    return pearsonr(x, y).statistic
res = permutation_test((x, y), statistic, vectorized=False,
                       permutation_type='pairings',
                       alternative='greater')

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    res = permutation_test((x, y), statistic, vectorized=False,
                       permutation_type='pairings',
                       alternative='greater')
    p = res.pvalue
    return p < 0.07
