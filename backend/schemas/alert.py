def alertEntity(item) -> dict:
    return {
        "id" : str(item["_id"]),
        "sensor_id" : str(item["sensor_id"]),
        "description" : item["description"],
        "date" : item["date"],
        "actions" : item["actions"]
    }

def alertsEntity(entity) -> list:
    return [alertEntity(item) for item in entity]