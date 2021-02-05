# Indigo research data

## To run
  1. **Create a virtual environment**

My preferred method for doing this is the following:
```sh
# from the root directory
python -m venv .
source bin/activate
```

But this should work fine inside conda, pipenv, etc.

  2. **Install dependencies**

```sh
python -m pip install -r requirements.txt
```

  3. **Run tests**

To make sure your environment is properly set up, try running the package's test suite

```
python -m pytest tests -vv
```

  4. **Run code**

With your virtual environment activated, run the main module
```sh
# optional: rm *.csv
# this will give you the full effect!

python -m indigo_research.main
```

The result should be 5 CSV files corresponding to the tables in `create_tables.sql`

## My workflow
  - Created the table structures on [DB Designer](https://www.dbdesigner.net/)
  - Ran the create_tables.sql script in MySQL to make sure everything worked
  - Wrote unit tests for the utility classes (`Loader` and `Validator`)
  - Toyed with a few ideas for the main `ResearchTable` class
  - After settling on a design, wrote test cases for each table it would produce
  - Iterated on the corresponding code and refined the tests until all tests passed 

## A few comments on design decisions

### Data model

I thought about normalizing the model even further, with tables for `Team` and `Farm` that would be referenced by the `Employee` and `Experiment` tables respectively, but seeing as they would mostly have made-up columns and be empty, it didn't seem worth it for the current scope of the problem.

Naming conventions are my own preferences, but I know some teams and DBMSs are more opinionated about such things

### CFU codes

After scratching my head with what to do with the non-numeric values in `average_cfu_per_seed`, I decided to punt the question and assign them specific codes that we could go over with business / data science users later. In the meantime, the negative values of all special codes means they can be easily filtered out of queries, provided the user remembers to do so.

### Design of the Python code

The Python code could probably be more elegant. As more data comes in and more consistent patterns of issues are discovered, it could make sense to abstract away some of the mappings and cleaning functions into more flexible classes. But given the size of the problem, the ad-hoc approach seemed to work reasonably well.

### Test-driven development

I tried to stick strictly to writing a set of tests and making sure the underlying functions adhered to them. The input data was a little too wide to do this comprehensively in the time I had to work on this, but I think the tests are clear and function as a good tutorial in using the `indigo_research` package. The file `seed_qa_tests_w_clean.xlsx` was created to be a "true negative" case for the validator. I had to make sure it didn't throw a warning when the underlying file was okay!
