import pymongo
from typing import List, Dict, Any

## Import rule variabel dari model.py
from model import SensorModel

## Koneksi database
client = pymongo.MongoClient("mongodb+srv://skilvul:skilvul@cluster0.wa4fqle.mongodb.net/?retryWrites=true&w=majority")

## Test DB Connection
# db = client.test
# print(db)

## Create DB
TDb = client["data-sensor"]

## Create Table
# Ganti 'mentor' dengan nama tim kalian
TSensor = TDb['mentor-2']

# Method CREATE
def db_create_sensor(sensor: SensorModel) -> bool:
    #insert_one -> masukkan data ke db
    TSensor.insert_one(sensor.__dict__)

# Methon READ
def db_list_sensors() -> List[SensorModel]:
    #find() -> menemukan/read semua data di tabel
    return [SensorModel.from_dict(r) for r in TSensor.find()]


## NEXT LESSON

# def db_update_sensor(sensor_id: str, sensor: Dict[str, Any]) -> bool:
#     res = TSensor.update_one({"id": sensor_id}, {"$set": sensor})
#     return res.modified_count > 0

# def db_retrieve_sensor(sensor_id: str) -> SensorModel:
#     _sensor = TSensor.find_one({"id": sensor_id})
#     return SensorModel.from_dict(_sensor) if _sensor else None

# def db_delete_sensor(sensor_id: str) -> bool:
#     res = TSensor.delete_one({"id": sensor_id})
#     return res.deleted_count > 0