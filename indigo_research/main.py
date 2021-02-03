import pandas as pd
import numpy as np
from indigo_research.research_table import ResearchTable
from indigo_research.utils import Loader
from indigo_research.utils import Validator


def main(path):
    loader = Loader(path)
    df = loader.load_data()

    employee = ResearchTable(df, "Employee")
    experiment = ResearchTable(df, "Experiment")
    sample = ResearchTable(df, "Sample")
    test = ResearchTable(df, "Test")

    employee.write()
    experiment.write()
    sample.write()
    test.write()


if __name__ == "__main__":
    main("seed_qa_tests.xlsx")
