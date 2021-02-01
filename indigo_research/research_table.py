import string
import pandas as pd

from indigo_research.mappings import employee_mapping
from indigo_research.mappings import experiment_mapping


# silence chained_assignment warning
pd.options.mode.chained_assignment = None


class ResearchTable:
    """A class to represent tables in the research schema

    It takes as input the name of a table in the schema and a Pandas dataframe
    with the columns required by that table. It will perform data processing
    according to the needs of that table

    It provides a general-purpose `write` method that can be used regardless
    of which specific table it represents
    """

    __VALID_NAMES = ["Employee", "Experiment", "Sample", "Test"]

    def __init__(self, raw_df, name):
        df = raw_df.copy(deep=True)
        df.columns = df.columns.str.lower()
        if name == "Employee":
            self.df = ResearchTable.__process_employee_data(df)
        elif name == "Experiment":
            self.df = ResearchTable.__process_experiment_data(df)
        elif name == "Sample":
            self.df = ResearchTable.__process_sample_data(df)
        elif name == "Test":
            self.df = ResearchTable.__process_test_data(df)
        else:
            raise ValueError(
                f"""{name} is not a table in the research schema.
            Did you mean one of these?
            {self.__VALID_NAMES}"""
            )
        self.name = name

    @staticmethod
    def __table_exists(name):
        for table in self.__VALID_NAMES:
            if name.lower() == table.lower():
                return True
        return False

    @staticmethod
    def __process_employee_data(df):
        employee_col = "sample received by"
        manager_col = "employee manager"
        team_col = "employee team"

        received_df = df[[employee_col, manager_col, team_col]]
        tested_df = df[["sample tested by", f"{manager_col}.1", f"{team_col}.1"]]
        tested_df.columns = received_df.columns

        employee_df = pd.concat([received_df, tested_df])

        employee_df.rename(
            columns={
                employee_col: "id",
                manager_col: "manager_id",
                team_col: "team_id",
            },
            inplace=True,
        )
        employee_df["name"] = ""
        employee_df["team_id"] = employee_df["team_id"].apply(
            lambda s: ResearchTable.__clean_string(s)
        )

        employee_df.replace(employee_mapping, inplace=True)

        return employee_df.drop_duplicates().dropna()

    @staticmethod
    def __process_experiment_data(df):

        df["sample_crop"].fillna(df["sample crop"], inplace=True)
        df["irp_barcode"].fillna(df["irp_qa_sample_barcode"], inplace=True)

        farm_col = "sample taken from farm#"
        treatment_col = "sample treatment_name"
        seed_col = "sample seed_variety"
        crop_col = "sample_crop"

        experiment_df = df[
            ["irp_barcode", farm_col, crop_col, treatment_col, seed_col,]
        ]

        experiment_df.rename(
            columns={
                farm_col: "from_farm_id",
                treatment_col: "sample_treatment",
                seed_col: "sample_seed_variety",
            },
            inplace=True,
        )

        experiment_df[crop_col] = experiment_df[crop_col].apply(
            lambda s: ResearchTable.__clean_string(s)
        )

        experiment_df.replace(experiment_mapping, inplace=True)

        # TODO deal with "n/a" in sample_treatment

        return experiment_df.drop_duplicates()  # .dropna()

    @staticmethod
    def __process_sample_data(df):

        received_col = "date_received_at_qa"
        days_between_col = "days between treatment and planting"
        received_by_col = "sample received by"

        df = df[
            [
                "irp_barcode",
                received_col,
                received_by_col,
                "date_treated",
                "date_planted",
                days_between_col,
                "date_sample_taken",
                "is_qa_needed",
            ]
        ]

        df.rename(
            columns={
                received_col: "date_received",
                days_between_col: "days_between_treated_and_planted",
                received_by_col: "received_by_employee_id",
            },
            inplace=True,
        )

        # TODO enforce days_between_treated_and_planted
        # TODO clean is_qa_needed
        # TODO date_treated strings...!

        return df

    @staticmethod
    def __process_test_data(df):
        received_col = "date_received_at_qa"
        tested_by_col = "sample tested by"
        seeds_col = "seeds/g"
        mass_col = "mass seed extracted"
        plated_vol_col = "plated volume"
        cfu_per_seed = "cfu/seed"

        df = df[
            [
                "irp_barcode",
                received_col,
                tested_by_col,
                "chemical_treatment_visible",
                "date_plated_on",
                "plating_code",
                seeds_col,
                mass_col,
                plated_vol_col,
                f"{cfu_per_seed} 1x",
                f"{cfu_per_seed} 10x",
                f"{cfu_per_seed} 100x",
                f"{cfu_per_seed} 1000x",
                "average_cfu_per_seed",
                "comment",
            ]
        ]

        df.rename(
            columns={
                received_col: "date_received",
                tested_by_col: "tested_by_employee_id",
                seeds_col: "seeds_per_gram",
                mass_col: "mass_seed_extracted",
                plated_vol_col: "plated_volume",
                f"{cfu_per_seed} 1x": "cfu_per_1_seed",
                f"{cfu_per_seed} 10x": "cfu_per_10_seed",
                f"{cfu_per_seed} 100x": "cfu_per_100_seed",
                f"{cfu_per_seed} 1000x": "cfu_per_1000_seed",
            },
            inplace=True,
        )

        # TODO deal with "grams", possibly rename column
        # TODO handle text entries...
        # TODO what to do with TCTC??

        return df

    @staticmethod
    def __clean_string(s):
        return ResearchTable.__remove_punctuation(s).upper().strip()

    @staticmethod
    def __remove_punctuation(s):
        exclude = set(string.punctuation)
        s = "".join(ch for ch in s if ch not in exclude)
        return s

    def write(self):
        self.df.to_csv(f"{self.name}.csv", index=False)


# TODO what if I instead did a general model class with named tables
