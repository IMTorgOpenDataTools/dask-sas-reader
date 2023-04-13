"""
Test additional functionality


"""

__author__ = "Jason Beach"
__version__ = "0.1.0"
__license__ = "MIT"


from dask_sas_reader import sas
import dask
from pathlib import Path


def test_dask_sas_reader_single_file():
    dir_path = Path('./tests/data') 
    file_path = dir_path / 'bond.sas7bdat'
    ddf = sas.dask_sas_reader(file_path, blocksize=5)
    recs = dask.compute(ddf.shape[0])[0] 
    assert recs == 102

def test_dask_sas_reader_multiple_files():
    dir_path = Path('./tests/data') 
    file_path = dir_path
    ddf = sas.dask_sas_reader(file_path, blocksize=5)
    recs = dask.compute(ddf.shape[0])[0] 
    assert recs == 204

def test_dask_sas_reader_pattern():
    dir_path = Path('./tests/data') 
    file_path = dir_path / 'bond-*'
    ddf = sas.dask_sas_reader(file_path, blocksize=5)
    recs = dask.compute(ddf.shape[0])[0] 
    assert recs == 102