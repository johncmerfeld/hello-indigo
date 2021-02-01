import pandas as pd
import warnings


class Validator:

    __EXPECDTED_COLS = [
        "sample Received By",
        "employee Manager",
        "employee Team",
        "irp_barcode",
        "sample taken from Farm#",
        "sample crop",
        "Sample treatment_name",
        "Sample seed_variety",
        "date_received_at_qa",
        "date_sample_taken",
        "date_treated",
        "date_planted",
        "Days between treatment and planting",
        "is_qa_needed",
        "sample tested By",
        "employee Manager.1",
        "employee Team.1",
        "chemical_treatment_visible",
        "date_plated_on",
        "plating_code",
        "Seeds/g",
        "Mass Seed Extracted",
        "Plated volume",
        "CFU/seed 1x",
        "CFU/seed 10x",
        "CFU/seed 100x",
        "CFU/seed 1000x",
        "average_cfu_per_seed",
        "comment",
    ]

    def __init__(self, test_df, expected_cols=__EXPECDTED_COLS, warn_only=True):
        df = test_df.copy(deep=True)
        df.columns = df.columns.str.lower()
        failed = False
        failed_msg = ""
        for col in Validator.__EXPECDTED_COLS:
            try:
                if df[col.lower()].isnull().all():
                    failed = True
                    failed_msg += f"{col} is entirely null\n"
            except KeyError:
                failed = True
                failed_msg += f"{col} not present in input dataframe\n"

        if failed:
            if warn_only:
                warnings.warn(failed_msg)
            else:
                raise ValueError(failed_msg)
