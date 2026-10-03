# mlops-labs

# MLOps Lab 1 – Testing and CI with GitHub Actions

Lab 1 for IE-7374 (MLOps). This project sets up a Python project with a virtual environment, unit tests written in both **pytest** and **unittest**, and **GitHub Actions** workflows that run the tests automatically on every push to `main`.

Instead of the calculator example from the original lab, this project uses a small text utilities module.

## Project Structure

```
mlops-labs/
├── .github/workflows/
│   ├── pytest_action.yml      # Runs pytest and uploads an XML report
│   └── unittest_action.yml    # Runs the unittest suite
├── data/                      # Placeholder for datasets
├── src/
│   └── text_utils.py          # Source code
├── test/
│   ├── test_pytest.py         # Tests written with pytest
│   └── test_unittest.py       # Tests written with unittest
├── .gitignore
├── requirements.txt
└── README.md
```

## Functions in `text_utils.py`

| Function | Description |
|---|---|
| `word_count(text)` | Returns the number of words in the text |
| `reverse_text(text)` | Returns the text reversed |
| `is_palindrome(text)` | Returns `True` if the text reads the same forwards and backwards, ignoring case, spaces, and punctuation |
| `text_summary(text)` | Combines the three functions above and returns the results as a dictionary |

Each function raises a `ValueError` if the input is not a string.

## Setup

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/Akshayaamahesh/mlops-labs.git
cd mlops-labs
python3 -m venv lab_01
source lab_01/bin/activate      # Mac / Linux
pip install -r requirements.txt
```

## Running the Tests Locally

Run all tests with pytest (this also picks up the unittest file):

```bash
pytest -v
```

Run only the unittest suite:

```bash
python -m unittest test.test_unittest
```

The pytest suite includes a parametrized test, which runs the same test function against multiple inputs.

## Continuous Integration with GitHub Actions

Two workflows run automatically whenever code is pushed to `main`:

- **Testing with Pytest** (`pytest_action.yml`) checks out the code, sets up Python, installs dependencies, runs pytest, and uploads a JUnit XML report (`pytest-report.xml`) as a downloadable artifact named `test-results`.
- **Python Unittests** (`unittest_action.yml`) checks out the code, sets up Python, installs dependencies, and runs the unittest suite.

Both workflows print a success or failure message at the end of the run. Results can be viewed under the **Actions** tab of this repository.

## Verifying That CI Catches Bugs

To confirm the pipeline works, I introduced a bug on purpose by removing `.lower()` from `is_palindrome`, which made the function case-sensitive.

- The **pytest** workflow failed, because its tests include mixed-case palindromes like "A man, a plan, a canal: Panama".
- The **unittest** workflow still passed, because its tests at the time only used lowercase inputs.

This showed that CI can only catch bugs that the tests are written to check for. I then fixed the bug and added a mixed-case test to the unittest suite, and both workflows passed again.
