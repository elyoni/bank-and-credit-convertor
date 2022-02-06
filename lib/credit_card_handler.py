#!/usr/bin/env python3
import pathlib
import pandas as pd
from datetime import datetime

class CreditCardMaxXlsxParser():
    ROW_START=3
    COLUMES_USE="A:B,F"
    COLUMES_INDEX=[0,2]
    @staticmethod
    def xlsx(file_path: pathlib.Path) -> pd.DataFrame:
        xls = pd.ExcelFile(file_path)
        custom_date_parser = lambda x: datetime.strptime(x, "%d-%m-%Y")
        df = pd.DataFrame()

        for sheet_name in xls.sheet_names:
            df = pd.concat(
                    [
                        df,
                        pd.read_excel(xls,
                            sheet_name=sheet_name,
                            header=CreditCardMaxXlsxParser.ROW_START,
                            usecols=CreditCardMaxXlsxParser.COLUMES_USE,
                            index_col=CreditCardMaxXlsxParser.COLUMES_INDEX,
                            names=["Date",
                                "Description",
                                "Amount",
                                ],
                            date_parser=custom_date_parser
                            )
                        ]
                    )
        return df
 
