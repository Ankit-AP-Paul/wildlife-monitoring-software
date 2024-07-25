def sensorEntity(item) -> dict:
    return {
        "id" : str(item["_id"]),
        "name" : item["name"],
        "latitude" : item["latitude"],
        "longitude" : item["longitude"],
        "region_id" : str(item["region_id"]),
        "radius" : item["radius"],
        "deployment_date" : item["deployment_date"],
        "status" : item["status"]
    }

def sensorsEntity(entity) -> list:
    return [sensorEntity(item) for item in entity]