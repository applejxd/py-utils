import dask.dataframe as dd
import pandas as pd
from .self_logger import SelfLogger
import pickle
import os

_logger = SelfLogger.get_logger(__file__)


def read_csv(file_name: str) -> pd.DataFrame:
    table = dd.read_csv(file_name).compute()
    _logger.info("CSV file read.")
    return table


def read_pickle(file_name: str) -> pd.DataFrame:
    if not os.path.exists("./output"):
        os.mkdir("./output")

    with open(f"./output/{file_name}.pkl", "rb") as f:
        result = pickle.load(f)
    _logger.info("Data read from a pickle.")
    return result


def write_pickle(data, file_name: str) -> None:
    if not os.path.exists("./output"):
        os.mkdir("./output")

    with open(f"./output/{file_name}.pkl", "wb") as f:
        pickle.dump(data, f)
    _logger.info("Data saved as a pickle.")
