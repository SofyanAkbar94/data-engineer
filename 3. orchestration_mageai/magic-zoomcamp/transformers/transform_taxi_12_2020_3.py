if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    zero_tripdistance_df = df[df['trip_distance'].isin([0])]
    zero_tripdistance_count = zero_tripdistance_df['trip_distance'].count()
    non_zero_tripdistance_df = df[df['trip_distance'] > 0]
    non_zero_tripdistance_count = non_zero_tripdistance_df['trip_distance'].count()
    print(f'Preprocessing: records with zero trip distance: {zero_tripdistance_count}')
    print(f'Preprocessing: records with trip distance more than zero: {non_zero_tripdistance_count}')

    return non_zero_tripdistance_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
