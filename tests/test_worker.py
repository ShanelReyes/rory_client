import pytest
from roryclient.client import RoryWorker
import time as T
from roryclient.models import EncryptDTO
worker = RoryWorker(hostname="localhost",port=9000)


# @pytest.mark.skip("")
def test_encrypt():
    res = worker.encrypt(
        dto = EncryptDTO(
            ball_id        = "bxx",
            bucket_id      = "rory",
            chunk_indexes  = [0,1,6],
            algorithm      = "LIU",
            security_level = 128
        )
    )
    print(res)