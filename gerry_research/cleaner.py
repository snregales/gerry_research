import pathlib as pl

import numpy as np
import pandas as pd

from gerry_research import collector
from gerry_research import constants as cnst

__all__ = ["clean"]


def str_to_number_column(df: pd.DataFrame, column: str) -> pd.Series:
    return df[column].str.replace(",", "").astype(np.int32)


def split_columns(df: pd.DataFrame, pattern: str, column: str):
    return df[column].str.split(pattern, expand=True)


def cleanup_scores(df: pd.DataFrame, pattern: str, column: str) -> pd.Series:
    return (
        df[column].replace(to_replace=pattern, value=r"\1", regex=True).astype(np.int8)
    )


def filter_less_or_equal_than(
    df: pd.DataFrame, column: str, number: int
) -> pd.DataFrame:
    return df.loc[df[column] > number]


def boolean_column(
    df: pd.DataFrame, data_path: pl.Path, indicator_column: str
) -> pd.Series:
    return df[indicator_column].isin(
        collector.read_excel(str(data_path), sheet_name=cnst.DATA_SHEET)[
            indicator_column
        ]
    )


def mark_early_access_column(df: pd.DataFrame) -> pd.Series:
    return boolean_column(df, cnst.EARLY_ACCESS, cnst.GAME_COLUMN)


def mark_indie_column(df: pd.DataFrame) -> pd.Series:
    return boolean_column(df, cnst.INDIE_FILE, cnst.GAME_COLUMN)


def clean_owner_datapoints(df: pd.DataFrame):
    df[[cnst.OWNER_LOWER_COLUMN, cnst.OWNER_UPPER_COLUMN]] = split_columns(
        df, pattern=r"\s\.\.\s", column=cnst.OWNER_COLUMN
    )
    df[cnst.OWNER_LOWER_COLUMN] = str_to_number_column(df, cnst.OWNER_LOWER_COLUMN)
    df[cnst.OWNER_UPPER_COLUMN] = str_to_number_column(df, cnst.OWNER_UPPER_COLUMN)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    clean_owner_datapoints(df)
    df[cnst.SCORE_COLUMN_CLEAN] = cleanup_scores(
        df, pattern=r"^.*\(.*(\d{2,3}).*\)$", column=cnst.SCORE_COLUMN
    )
    df[cnst.EARLY_ACCESS_COLUMN] = mark_early_access_column(df)
    df[cnst.INDIE_COLUMN] = mark_indie_column(df)
    df = filter_less_or_equal_than(df, column=cnst.OWNER_LOWER_COLUMN, number=20_000)
    return df[cnst.EXPORT_COLUMNS]
