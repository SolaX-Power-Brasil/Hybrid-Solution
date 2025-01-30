
"""
Common attributes for all tests
"""

inverters_rated_power = {
    "X1-HYBRID-5.0-D":  5000, 
    "X1-HYBRID-7.5-D":  7500,
    "X1-SPT-6K":        6000,
    "X3-HYBRID-15.0-D": 15000
}

x1_overload =  1.5, 
spt_overload = 1.2, 
x3_overload =  1.5

inverters_peak_power = {
    "X1-HYBRID-5.0-D":  inverters_rated_power['X1-HYBRID-5.0-D' ] * x1_overload, 
    "X1-HYBRID-7.5-D":  inverters_rated_power['X1-HYBRID-7.5-D' ] * x1_overload,
    "X1-SPT-6K":        inverters_rated_power['X1-SPT-6K'       ] * spt_overload,
    "X3-HYBRID-15.0-D": inverters_rated_power['X3-HYBRID-15.0-D'] * x3_overload
}

batteries_standard_power = {
    "T58": 2875
}

files = {
    "../singlePhaseHVBat.json",
    "../splitPhaseHVBat.json",
    "../threePhaseHVBat.json"
}