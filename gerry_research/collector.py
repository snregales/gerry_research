# %%
import pathlib
from io import StringIO

import pandas as pd
from xlsx2csv import Xlsx2csv

from gerry_research import constants as cnst


# https://stackoverflow.com/questions/28766133/faster-way-to-read-excel-files-to-pandas-dataframe
def read_excel(
    path: str, sheet_name: str, na_values: list[str] = None, dropna: bool = True
) -> pd.DataFrame:
    buffer = StringIO()
    (Xlsx2csv(path, outputencoding="utf-8", sheet_name=sheet_name).convert(buffer))
    buffer.seek(0)
    data = pd.read_csv(buffer, na_values=na_values or [])
    return (
        data.dropna(
            subset=[
                cnst.SCORE_COLUMN,
            ],
        ).reset_index()
        if dropna
        else data
    )


def collect_all_data_files(
    files: list[pathlib.Path], duplcate_subset: list[str] = None
) -> pd.DataFrame:
    return pd.concat(
        (
            read_excel(
                file_, sheet_name=cnst.DATA_SHEET, na_values=["N/A", "N/A (N/A)"]
            )
            for file_ in files
        ),
        ignore_index=True,
    ).drop_duplicates(subset=duplcate_subset)


def merge_output_files(df: pd.DataFrame):
    df_left = read_excel(
        str(cnst.INCOMING_OUTPUT_FILE), sheet_name=cnst.DATA_SHEET, dropna=False
    )
    df_left.rename(columns=cnst.GAME_COLUMN_RENAME, inplace=True)
    return pd.merge(df, df_left[cnst.INCOMING_OUTPUT_FILE_COLUMNS], on=cnst.GAME_COLUMN)
