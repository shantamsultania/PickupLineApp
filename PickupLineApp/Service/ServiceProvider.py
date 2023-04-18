import random

from PickupLineApp.helper.HelperClass import list_of_pickup_lines as pickup_lines


# This will Handle the CRUD APP working

# C = Create
# R = Read
# U = Update
# D = Delete


# get multiple PickupLines
def get_pickup_lines():
    return pickup_lines


# get a PickupLine
def get_pickup_line():
    return random.choice(pickup_lines)


# add a PickupLine
def add_PickupLines(pickup_line):
    pickup_lines.append(pickup_line)
    return f'PickupLine has been added to the database new PickupLine = {pickup_lines[len(pickup_lines) - 1]}'


# update a PickupLine
def update_PickupLine(pickup_line_to_be_updated, updated_pickup_line):
    for idx, item in enumerate(pickup_lines):
        if pickup_line_to_be_updated == item:
            pickup_lines[idx] = updated_pickup_line
    return get_pickup_lines()


# delete a PickupLine
def delete_PickupLine(pickup_line):
    previous_count = len(pickup_lines)
    pickup_lines.remove(pickup_line)
    return f'PickupLine has been removed from the database old count = {previous_count} new count = {len(pickup_lines)} '
