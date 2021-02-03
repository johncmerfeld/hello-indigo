import numpy as np
import pandas as pd

employee_mapping = {"MP": "Marion P"}

experiment_mapping = {
    "Sylvester PhotonAX HRW": "Sylvester PhotonAX HRWW",
    "Sylvester Langin": "Sylvester Langin HRWW",
    "Sylvester Tam 114 HRWW": "Sylvester Tam114 HRWW",
}

sample_mapping = {
    "YES": True,
    "TRUE": True,
    "NO": False,
    "FALSE": False,
    "NAN": np.nan,
    "Unknown": pd.NaT,
}

test_mapping = {
    "TCTC": -999,
    "TNTC": -999,
    "Contaminated": -998,
    "Inconclusive": -997,
    "++": -996,
}
