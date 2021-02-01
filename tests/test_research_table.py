import pandas as pd
import numpy as np
import pytest
from indigo_research.research_table import ResearchTable
from indigo_research.utils import Loader
from indigo_research.utils import Validator


@pytest.fixture
def test_data():
    loader = Loader("seed_qa_tests.xlsx")
    return loader.load_data()


def test_valid_table_names():
    # an invalid table name will throw an error
    try:
        rt2 = ResearchTable(pd.DataFrame(), "InvalidName")
        assert False
    except ValueError:
        assert True


def test_process_employee_data(test_data):
    employee = ResearchTable(test_data, "Employee")
    assert set(employee.df.columns) == set(["id", "name", "manager_id", "team_id"])
    print(f"\n{employee.df.to_string()}")
    assert employee.df.shape == (3, 4)


def test_process_experiment_data(test_data):
    experiment = ResearchTable(test_data, "Experiment")
    assert set(experiment.df.columns) == set(
        [
            "irp_barcode",
            "from_farm_id",
            "sample_crop",
            "sample_treatment",
            "sample_seed_variety",
        ]
    )
    print(f"\n{experiment.df.to_string()}")
    assert experiment.df.shape == (274, 5)


def test_process_sample_data(test_data):
    sample = ResearchTable(test_data, "Sample")
    assert set(sample.df.columns) == set(
        [
            "irp_barcode",
            "date_received",
            "received_by_employee_id",
            "date_treated",
            "date_planted",
            "days_between_treated_and_planted",
            "date_sample_taken",
            "is_qa_needed",
        ]
    )
    print(f"\n{sample.df.to_string()}")
    assert sample.df.shape == (377, 8)
    assert set(list(sample.df["is_qa_needed"])) == set([True, False, np.nan])


def test_process_test_data(test_data):
    test = ResearchTable(test_data, "Test")
    assert set(test.df.columns) == set(
        [
            "irp_barcode",
            "date_received",
            "tested_by_employee_id",
            "date_plated_on",
            "chemical_treatment_visible",
            "plating_code",
            "seeds_per_gram",
            "mass_seed_extracted",
            "plated_volume",
            "cfu_per_1_seed",
            "cfu_per_10_seed",
            "cfu_per_100_seed",
            "cfu_per_1000_seed",
            "average_cfu_per_seed",
            "comment",
        ]
    )

    test.df.drop(columns=["comment"], inplace=True)
    print(f"\n{test.df.to_string()}")
    assert test.df.shape == (377, 15)
