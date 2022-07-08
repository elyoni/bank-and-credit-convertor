#!/usr/bin/env python3
import pandas as pd
from src.credit_card_handler import CreditCardMaxXlsxParser
def test_credit_card_parser():
    df = CreditCardMaxXlsxParser.xlsx("test/max-credit-card_test.xlsx")
    data={
            "Description": ["Work", "Do", "Something", "fun fun", "English Line", "AMZN  AMZN.COMBILL US", "AMZN  AMZN.COM/BILL US", "ALIEXPRESS", "GOOGLE"],
            "Date": ["21-03-2021", "01-12-2021", "04-01-2022", "06-01-2022", "06-01-2022", "15-12-2021", "16-12-2021", "16-12-2021", "27-12-2021"],
            "Amount": [200, 201, 202, 203, 203, 600, 601, 602, 603]
            }
    df_expected = pd.DataFrame(data=data)
    df_expected.set_index(["Date", "Amount"], inplace=True)
    assert df_expected.equals(df_expected)
