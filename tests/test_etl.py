from src.etl import load_sample_data


def test_load_sample_data_returns_dataframe():
    df = load_sample_data()

    assert not df.empty
    assert list(df.columns) == ["product_id", "quantity"]
