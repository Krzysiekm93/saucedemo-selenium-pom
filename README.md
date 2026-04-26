# saucedemo-selenium-pom

Selenium-based UI automation project for the SauceDemo website using the Page Object Model (POM) design pattern.

This repository contains automated UI tests for key user flows such as login, inventory, cart, and checkout.

## What Is Covered

- Page Object Model structure for core SauceDemo pages (`LoginPage`, `InventoryPage`, `CartPage`, checkout pages)
- Data-driven login tests using CSV credentials from `test_data/login.csv` (including locked-out user handling)
- Inventory validations: sorting by name and price, with product order checks
- Cart workflows: adding random products, cart badge/count checks, and item removal behavior
- Checkout flow coverage: customer information step, overview step, and finish/complete validation
- Cross-target execution with pytest `--target` option (`desktop`, `mobile`, `both`)

## Tech Stack

- Python 3
- Selenium WebDriver
- pytest
- Chrome / ChromeDriver

## Project Structure

```text
saucedemo-selenium-pom/
├── pages/                # Page Object classes
├── tests/                # Test modules + pytest fixtures/hooks
├── test_data/            # CSV files and data helpers
├── utils/                # Shared helper utilities
├── pytest.ini            # Pytest configuration
├── requirements.txt      # Python dependencies
└── README.md
```

## Prerequisites

- Python 3.10+ (or project-compatible Python 3)
- Google Chrome installed
- Matching ChromeDriver available through Selenium Manager (default Selenium behavior) or your local setup

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Tests

Run commands from the project root (`saucedemo-selenium-pom`).

Required execution commands:

```bash
pytest --target=desktop
pytest --target=mobile
pytest --target=both
```

## Optional Useful Commands

```bash
pytest -v --target=desktop
pytest -k "login" --target=both
pytest tests/test_login.py --target=mobile
```

## Notes on Targets

The `--target` option is used by pytest fixture/hook logic in `tests/conftest.py`:

- `desktop`: runs tests with standard desktop Chrome
- `mobile`: runs tests with Chrome mobile emulation
- `both`: runs both variants where applicable

## Test Data

- Login data is stored in `test_data/login.csv`.
- Helper functions in `test_data/login_data.py` are used to load credentials in tests/fixtures.

## Recommended Workflow

```bash
source .venv/bin/activate
pytest --target=desktop
pytest --target=mobile
pytest --target=both
```
