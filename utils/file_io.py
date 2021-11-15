import dask.dataframe as dd
import pandas as pd
from .self_logger import SelfLogger
import pickle
import os

_logger = SelfLogger.get_logger(__file__)


def make_dir(dir_name: str) -> None:
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        _logger.info(f"Made dir: {dir_name}")


def read_csv(file_name: str) -> pd.DataFrame:
    table = dd.read_csv(file_name).compute()
    _logger.info(f"Read CSV: {file_name}")
    return table


def read_pickle(file_name: str) -> pd.DataFrame:
    make_dir("./output")
    with open(f"./output/{file_name}", "rb") as f:
        result = pickle.load(f)
    _logger.info(f"Read pickle: {file_name}")
    return result


def write_pickle(data, file_name: str) -> None:
    make_dir("./output")
    with open(f"./output/{file_name}", "wb") as f:
        pickle.dump(data, f)
    _logger.info(f"Write pickle: {file_name}")
