#!/usr/bin/env python3
import pathlib
import pandas as pd
from datetime import datetime

class BankLeumiXlsxParser():
    ROW_START=17
    COLUMES_USE="A,B,D,E"
    #  COLUMES_INDEX=[0,2]
    @staticmethod
    def xlsx(file_path: pathlib.Path) -> pd.DataFrame:
        '''Convert Leumi Bank excel sheets into dataframe'''
        xls = pd.ExcelFile(file_path)
        custom_date_parser = lambda x: datetime.strptime(x, "%d-%m-%Y")
        df = pd.DataFrame()

        for sheet_name in xls.sheet_names:
            df = pd.concat(
                    [
                        df,
                        pd.read_excel(xls,
                            sheet_name=sheet_name,
                            header=BankLeumiXlsxParser.ROW_START,
                            usecols=BankLeumiXlsxParser.COLUMES_USE,
                            #  index_col=BankLeumiXlsxParser.COLUMES_INDEX,
                            na_values=0,
                            names=["Date",
                                "Description",
                                "Debt",
                                "Credit",
                                ],
                            date_parser=custom_date_parser
                            )
                        ]
                    )
            df.fillna(0, inplace=True)
            df["Amount"] = df["Credit"] - df["Debt"]
            df.drop(columns=["Credit", "Debt"], inplace=True)
            df.set_index(["Date", "Amount"], inplace=True)
        return df
