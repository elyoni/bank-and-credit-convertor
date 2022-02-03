#!/usr/bin/env python3
import pandas as pd
from lib.dataframe_convertor import DataConvertor
def test_dataconvertor_append():
    df_reference = pd.DataFrame(
            index=["day01", "day02", "day03", "day04"],
            data={
                "description": ["description01", "description02", "description03", "description04"],
                "amount": ["amount01", "amount02", "amount03", "amount04"],
                }
            )
    df_new_values = pd.DataFrame(
            index=["day03", "day04", "day05"],
            data={
                "description": ["description03", "description04", "description05"],
                "amount": ["amount03", "amount04", "amount05"],
                }
            )
    df_expected = pd.DataFrame(
            index=["day05"],
            data={
                "description": ["description05"],
                "amount": ["amount05"],
                }
            )

    assert df_expected.equals(DataConvertor.clean_old(df_reference, df_new_values))
