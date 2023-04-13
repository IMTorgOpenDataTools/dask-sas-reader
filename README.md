# Dask SAS Reader

Read SAS files into a Python Dask DataFrame.

## Usage

Install from PyPI: `https://pypi.org/project/dask-sas-reader/0.1.0/`

```
pip install dask_sas_reader
```

Import and use module.

```
import dask_sas_reader

import dask
import dask.dataframe as dd
from dask.delayed import delayed


data_dir = Path('../data')
file_path = data_dir / 'bond.sas7bdat'

dd_df = sas.dask_sas_reader(data_dir, blocksize=800000)
dd_df.head()
```


## Build

Build and install locally with:

```
(dask-sas-reader) $ pipenv shell
(dask-sas-reader) $ pipenv run python -m build --wheel
(dask-sas-reader) $ exit
$ pip install dask-sas-reader/dist/dask_sas_reader-*.whl
```


## Test

Test simply using:

```
pytest --collect-only
pytest
```