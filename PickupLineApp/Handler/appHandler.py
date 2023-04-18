from PickupLineApp.Service.ServiceProvider import get_pickup_lines, get_pickup_line, add_PickupLines, delete_PickupLine, \
    update_PickupLine
from flask import Flask, request

app = Flask(__name__)


@app.route("/getPickupLines", methods=['GET'])
def handle_get_all():
    return get_pickup_lines()


@app.route("/getPickupLine", methods=['GET'])
def handle_get_one():
    return get_pickup_line()


@app.route("/addPickupLine", methods=['POST'])
def handle_add_pickup_lines():
    request_data = request.json
    line = request_data['addPickupLine']
    return add_PickupLines(line)


@app.route("/updatePickupLines", methods=['PUT'])
def handle_update_line():
    request_data = request.json
    return update_PickupLine(request_data['updatePickupLine'], request_data['updatePickupLinesWith'])


@app.route("/deletePickupLines", methods=['DELETE'])
def handle_delete_line():
    request_data = request.json
    return delete_PickupLine(request_data["deletePickupLine"])
