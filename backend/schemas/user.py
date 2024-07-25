def userEntity(item) -> dict:
    return {
        "name":item["name"],
        "email":item["email"],       
        "phone_no":item["phone_no"],
        "region_id":str(item["region_id"]),
        "gov_body":item["gov_body"],
        "created_at":item["created_at"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]