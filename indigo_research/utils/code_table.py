import pandas as pd

code_dict = {
    "code": [-999, -998, -997, -996],
    "description": ["Too many colonies to count", "Contaminated", "Inconclusive", "++"],
}


def create_code_table(codes=code_dict):
    df = pd.DataFrame(code_dict)
    return df
