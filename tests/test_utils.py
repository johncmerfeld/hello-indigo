import pandas as pd
import pytest
import warnings
from indigo_research.utils import Loader
from indigo_research.utils import Validator
from indigo_research.utils import create_code_table


@pytest.fixture
def default_path():
    return "seed_qa_tests_w_clean.xlsx"


def test_loader(default_path):
    loader = Loader(default_path)
    df = loader.load_data()
    assert df.shape == (723, 31)


# ordinarily, the validator merely raises a warning
def test_validator(default_path):
    df_dict = pd.read_excel(default_path, sheet_name=None)
    with pytest.warns(None) as record:
        for df in df_dict:
            Validator(df_dict[df], warn_only=True)
    # how many errors were raised while reading these two dataframes?
    assert len(record) == 2


# test the validator's "strict" setting
def test_validator_with_error(default_path):
    df_dict = pd.read_excel(default_path, sheet_name=None)
    try:
        for df in df_dict:
            Validator(df_dict[df], warn_only=False)
        assert False
    except ValueError:
        assert True


# test static cfu_code table creator
def test_code_table():
    df = create_code_table()
    assert df.shape == (4, 2)
    assert set(["code", "description"]) == set(list(df.columns))
