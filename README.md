# retail-mini-etl

This is a beginner-friendly Python ETL starter project.

## Project structure

- src/: Python source code
- tests/: pytest tests
- data/raw/: raw input data
- data/processed/: processed output data
- db/: SQLite database files
- docs/: project notes

## Run steps

1. Create and activate a virtual environment:
   - python -m venv .venv
   - .venv\\Scripts\\activate

2. Install dependencies:
   - pip install -r requirements.txt

3. Run the ETL script:
   - python -m src.etl

4. Run tests:
   - pytest
