def regionEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "description":item["description"],
        "wildlife":item["wildlife"],
        "birds":item["birds"]
    }

def regionsEntity(entity) -> list:
    return [regionEntity(item) for item in entity]