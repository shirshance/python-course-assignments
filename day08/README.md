# Cell Splitting Calculator Web App

## Description

This project is a web version of my Cell Splitting Calculator.

The calculator determines how much cell suspension to take and how much fresh medium to add based on a desired split ratio.

Example:

* Final volume: 10 mL
* Split ratio: 1:10

Result:

* Take 1 mL of cells
* Add 9 mL of fresh medium

## Files

* `cell_split_lib.py` – business logic
* `cell_split_web.py` – FastAPI web application
* `test_cell_split_web.py` – web application tests
* `requirements.txt` – project dependencies

## Run

Install dependencies:

```bash
pip3 install -r requirements.txt
```

Start the web app:

```bash
python3 -m uvicorn cell_split_web:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## Tests

Run:

```bash
pytest
```

## AI Usage

I used ChatGPT to:

* Convert the calculator into a FastAPI web application
* Write tests using FastAPI TestClient
* Add input validation
* Help prepare the README
