#!/usr/bin/Python

import numpy as np
import pandas as pd
from nose.tools import assert_equal

from calculationGDD import calculate_GDD


def test_GDD():
    baseTemp = 10;
    obs = {'Max Temp (°C)' : pd.Series([13.1, 4.9, 13.4, 20.7, 27.9]),
           'Min Temp (°C)' : pd.Series([0.7, -1.6, -5.6, -0.6, 3.1])}
    obs_df = pd.DataFrame(obs)
  
    test_obs = calculate_GDD(obs_df, baseTemp)
    obs_GDD = list(np.array(test_obs['GDD']))
    
    exp_GDD = [1.5500000000000007, 0.0, 1.6999999999999993, 5.3499999999999996, 8.9499999999999993]

    assert_equal(exp_GDD, obs_GDD)


test_GDD()
