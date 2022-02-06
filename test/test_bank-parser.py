#!/usr/bin/env python3
import pandas as pd
from lib.bank_handler import BankLeumiXlsxParser
def test_credit_card_parser():
    df = BankLeumiXlsxParser.xlsx("test/leumi_bank_test.xlsx")

    data = {
            "Description": ["work01", "work02", "work03", "card", "card1", "card2", "card3", "card4", "health"],
            "Date": ["01/07/20", "01/07/20", "01/07/20", "03/07/23", "03/07/23", "03/07/23", "03/07/23", "03/07/23", "01/07/28"],
            "Amount": [1.0, 2.0, 3.0, -1.0, -2.0, -3.0, -4.0, -5.0, -6.0]
    }
    df_expected = pd.DataFrame(data=data)
    df_expected.set_index(["Date", "Amount"], inplace=True)
    assert df_expected.equals(df_expected)
