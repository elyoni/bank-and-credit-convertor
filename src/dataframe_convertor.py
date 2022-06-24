#!/usr/bin/env python3
import pandas as pd
from loguru import logger


class DataConvertor():
    @staticmethod
    def clean_old(df_reference: pd.DataFrame, df_new_value: pd.DataFrame) -> pd.DataFrame:
        """
        Remove duplicated rows, only new rows will remain
        Uses to clean the new data
        Note: To use this function you have to configure the index's of both of the data frame
        """
        df_clean = pd.DataFrame()
        if not df_reference.empty:
            # Check which row is already in the global database
            logger.debug(f"\ndf_reference:\n{df_reference}")
            logger.debug(f"\ndf_new_value:\n{df_new_value}")
            df_clean = df_reference.merge(df_new_value,
                    left_index=True,
                    right_index=True,
                    how='right', indicator=True,
                    suffixes=("_left", ""))
            # Remove merge left over
            logger.debug(f"\ndf_clean:\n{df_clean}")
            df_clean.drop(df_clean.filter(regex='_left$').columns.tolist(),
                    axis=1,
                    inplace=True)
            df_clean = df_clean.loc[df_clean["_merge"] == "right_only"].drop(columns="_merge")

        logger.debug(f"\ndf_merged:\n{df_clean}")
        return df_clean
