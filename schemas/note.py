def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "desc": item["desc"],
        "important": item["important"]
    }

def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]
