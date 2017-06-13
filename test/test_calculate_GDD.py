import pandas as pd
import numpy as np
import sys
from nose.tools import assert_equal
sys.path.append('./Desktop/important/project')
from calculationGDD import calculate_GDD


def test_calculate_GDD():
    baseTemp = 10
    # Observed Min, Max values for test purpose. 
    obs = {'Max Temp (Â°C)' : pd.Series([13.1, 4.9, 13.4, 20.7, 27.9, 18.4, 15.8, 17.9, 11.8, 15.1, 21.5, 19.8, 10.6, 15.7, 14.9]),
           'Min Temp (Â°C)' : pd.Series([0.7, -1.6, -5.6, -0.6, 3.1, 3.4, -1.2, 2.4, 0.5, -1.4, 0.1, 3, 0.6, -3.2, 1])}
    obs_df = pd.DataFrame(obs)
    
    test_obs = calculate_GDD(obs_df, baseTemp)
    
    obs_GDD = np.array(test_obs['GDD'])
    obs_GDD = list(obs_GDD)
    
    # Sample expected values including manually calculated GDD values to compare with Observed values. 

    exp_GDD = [0.0, 0.0, 0.0, 0.049999999999998934, 5.5499999999999989, 6.4499999999999975, 6.4499999999999975, 6.5999999999999961, 6.5999999999999961, 6.5999999999999961, 7.3999999999999968, 8.7999999999999972, 8.7999999999999972, 8.7999999999999972, 8.7999999999999972]

    assert_equal(exp_GDD, obs_GDD)

test_calculate_GDD()
