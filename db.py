import pymongo
client = pymongo.MongoClient("mongodb+srv://skilvul:skilvul@cluster0.wa4fqle.mongodb.net/?retryWrites=true&w=majority")

## Test DB Connection
# db = client.test
# print(db)

from model import SensorModel
from typing import List, Dict, Any

## Create DB
TDb = client["data-sensor"]

## Create Table
# Ganti dengan nama tim kalian
TSensor = TDb['mentor']

# Method CREATE
def db_create_sensor(sensor: SensorModel) -> bool:
    TSensor.insert_one(sensor.__dict__)

# Methon READ
def db_list_sensors() -> List[SensorModel]:
    return [SensorModel.from_dict(r) for r in TSensor.find()]

# def db_update_sensor(sensor_id: str, sensor: Dict[str, Any]) -> bool:
#     res = TSensor.update_one({"id": sensor_id}, {"$set": sensor})
#     return res.modified_count > 0

# def db_retrieve_sensor(sensor_id: str) -> SensorModel:
#     _sensor = TSensor.find_one({"id": sensor_id})
#     return SensorModel.from_dict(_sensor) if _sensor else None


# def db_delete_sensor(sensor_id: str) -> bool:
#     res = TSensor.delete_one({"id": sensor_id})
#     return res.deleted_count > 0