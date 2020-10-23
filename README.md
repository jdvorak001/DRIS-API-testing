# DRIS-API-testing 

[![image](https://img.shields.io/pypi/v/pipenv.svg)](../..)
[![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/jdvorak001/DRIS-API-testing)](../..)

A light-weight tool to test-drive the DRIS+ API.

Here DRIS+ stands for the [Directory of Research Information Systems](https://dspacecris.eurocris.org/cris/explore/dris), a service run by [euroCRIS](https://www.eurocris.org/).

## Installation and running

1. Checkout this project
2. Run the Pipenv environment (``pipenv shell``) and do the rest of this procedure from within there
3. Run ``./download.py`` to retrieve the whole contents of the API into a `raw-data/` directory
4. Run ``./process.py`` to process the retrieved contents from `raw-data/` into individual, pretty-printed entries in a `data/` directory
5. Run ``./download2.py`` to re-retrieve the individual records from the `data/` directory (overwriting the original files)
