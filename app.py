from flask import Flask, request, jsonify
from model import SensorModel
from db import db_create_sensor, db_list_sensors, db_retrieve_sensor, db_update_sensor, \
    db_delete_sensor

app = Flask(__name__)

### Routing dan Method CRUD

## "CREATE" data/post data ke database
@app.route("/create", methods=["POST"])
def create_sensor():
    """"
    Create a new sensor
    """
    data = request.get_json()
    status = SensorModel.Schema().validate(data)
    if status:
        return jsonify(status), 404
    sensor = SensorModel.from_dict(data)
    db_create_sensor(sensor)
    return jsonify(data=sensor.to_dict()), 200

## "GET" ambil data dari database
@app.route("/list", methods=["GET"])
def list_sensor():
    """"
    Retrieve all sensors
    """
    # Find/get all data di sensor disimpan di var sensor
    sensors = db_list_sensors()
    res = {"data-all-sensor": [sensor.to_dict() for sensor in sensors], "count": len(sensors)}
    return jsonify(data=res), 200

if __name__ == "__main__":
    app.run(debug=True)

## NEXT LESSON

# @app.route("/retrieve", methods=["GET"])
# def retrieve_sensor():
#     """"
#     Retrieve a sensor
#     """
#     sensor_id = request.args.get("id")
#     sensor = db_retrieve_sensor(sensor_id)
#     if sensor:
#         return jsonify(data=sensor.to_dict()), 200
#     return jsonify({"message": "Book not found"}), 404


# @app.route("/update", methods=["POST"])
# def update_sensor():
#     """"
#     Update a sensor
#     """
#     payload = request.get_json()
#     status = SensorModel.Schema().validate(payload)
#     if status:
#         return jsonify(status), 400
#     sensor_id = payload.get("id")
#     if not db_retrieve_sensor(sensor_id):
#         return jsonify({"message": "Book not found"}), 404

#     success = db_update_sensor(sensor_id, payload)
#     if not success:
#         return jsonify({"message": "Book Update failed"}), 404
#     sensor_db = db_retrieve_sensor(sensor_id)
#     return jsonify(data=sensor_db.to_dict()), 200


# @app.route("/delete", methods=["DELETE"])
# def delete_sensor():
#     """"
#     Delete a sensor
#     """
#     sensor_id = request.args.get("id")
#     if not sensor_id:
#         return jsonify({"message": "Book id is required"}), 400
#     success = db_delete_sensor(sensor_id)
#     if not success:
#         return jsonify({"message": "Book Delete failed"}), 404
#     return jsonify({"message": "Book Deleted"}), 200

