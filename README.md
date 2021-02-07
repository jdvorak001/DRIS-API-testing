# DRIS-API-testing 

[![image](https://img.shields.io/pypi/v/pipenv.svg)](../..)
[![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/jdvorak001/DRIS-API-testing)](../..)

A light-weight tool to test-drive the DRIS+ API.

Here DRIS+ stands for the [Directory of Research Information Systems](https://dspacecris.eurocris.org/cris/explore/dris), a service operated by [euroCRIS](https://www.eurocris.org/).

## Installation and running

1. Checkout this project
2. Run the [Pipenv](https://pipenv.pypa.io/en/latest/) environment (``pipenv shell``) and do the rest of this procedure from within there:
3. Run ``./download.py`` to retrieve the whole contents of the API into a `raw-data/` directory
4. Run ``./process.py`` to process the retrieved contents from `raw-data/` into individual, pretty-printed entries in a `data/` directory
5. Run ``./download2.py`` to re-retrieve the individual records from the `data/` directory (overwriting the original files). If your DRIS_CREDENTIALS environment variable contains a `username`:`password` pair, it is used for basic HTTP authentication with the API endpoint.
6. Run ``./list-openaireCrisEndpointURLs.sh`` to summarize the different values of the openaireCrisEndpointURL field in JSON files in the `data/` directory

After having run step 5 with authentication, please ensure the data with the openaireCrisEndpointURL fields filled in do not accidentally get committed in the git repo.
