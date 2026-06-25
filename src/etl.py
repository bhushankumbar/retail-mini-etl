from pathlib import Path

import pandas as pd


def load_sample_data() -> pd.DataFrame:
    """Return a small example dataset for the ETL starter project."""
    return pd.DataFrame(
        [
            {"product_id": 101, "quantity": 2},
            {"product_id": 102, "quantity": 5},
        ]
    )


def main() -> None:
    df = load_sample_data()
    output_path = Path("data/processed/sample.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Wrote {len(df)} rows to {output_path}")


if __name__ == "__main__":
    main()
