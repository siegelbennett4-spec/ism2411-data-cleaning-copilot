import os
import pandas as pd
from src import data_cleaning


def test_pipeline_creates_clean_file(tmp_path):
    # Arrange: use the included raw CSV and a temporary output path
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    raw_path = os.path.join(repo_root, "data", "raw", "sales_data_raw.csv")
    out_path = tmp_path / "cleaned.csv"

    # Act: run the pipeline function to produce cleaned output
    df = data_cleaning.run_cleaning_pipeline(raw_path, str(out_path))

    # Assert: output file exists and contains no negative quantities/prices
    assert out_path.exists()
    assert (df['quantity'] >= 0).all()
    assert (df['price'] >= 0).all()
    # price should have no nulls
    assert df['price'].notna().all()
