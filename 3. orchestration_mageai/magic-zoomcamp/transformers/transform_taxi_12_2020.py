import pandas as pd
from pandas import DataFrame
from datetime import datetime

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):

    df.columns = (df.columns
                .str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True)
                .str.lower()
             )
    df['lpep_pickup_date'] = df['lpep_pickup_datetime'].dt.date
    return df


@test
def test_output(output, *args):
    assert output is not None, 'The output is undefined'