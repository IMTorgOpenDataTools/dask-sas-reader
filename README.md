# Dask SAS Reader

Read SAS files into a Python Dask DataFrame.

## Usage

Install from PyPI

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


## Test

Test simply using:

```
pytest --collect-only
pytest
```