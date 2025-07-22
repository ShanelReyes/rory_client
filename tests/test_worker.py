import pytest
from roryclient.client import RoryWorker
import time as T
from roryclient.models import EncryptDTO,KMeansDTO
@pytest.fixture
def worker():
    w= RoryWorker(hostname="localhost",port=9000)
    return w


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



# @pytest.mark.skip("")
def test_encrypt(worker):
    dto = EncryptDTO(chunk_indexes=[0], bucket_id="rory",ball_id="bxx",algorithm="LIU",security_level=128)  # Adjust fields
    result = worker.encrypt(dto)

@pytest.mark.skip("")
def test_kmeans(worker):
    dto = KMeansDTO(data=[[1, 2], [3, 4]], clusters=2)
    result = worker.kmeans(dto)

def test_worker_get_tasks(worker):
    result = worker.get_tasks()

def test_worker_get_task_details(worker):
    result = worker.get_task_details()

def test_worker_get_completed_tasks(worker):
    result = worker.get_completed_tasks()