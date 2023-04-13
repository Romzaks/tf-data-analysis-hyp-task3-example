import pandas as pd
import numpy as np
import scipy.stats as stat

chat_id = 333357078 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    return stat.ttest_ind(x, y, equal_var=False, alternative='greater')[1] < 0.07
