import pandas as pd
from indigo_research.utils import Validator


class Loader:
    def __init__(self, path, validate=False):
        self.path = path
        self.validate = validate

    def load_data(self):
        df_dict = pd.read_excel(self.path, sheet_name=None)
        if type(df_dict) == pd.DataFrame:
            result = df_dict
        elif type(df_dict) == dict:
            result = pd.concat(df_dict.values())
            result.reset_index(inplace=True, drop=True)
        else:
            raise ValueError(f"Your excel file was loaded in as a {type(df_dict)}")

        if self.validate:
            # this will throw a warning if it fails
            Validator(result, warn_only=True)
        return result
