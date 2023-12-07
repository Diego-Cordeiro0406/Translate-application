from database.db import db
from models.abstract_model import AbstractModel


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data):
        super().__init__(data)

    def to_dict(self):
        return {"name": self.data["name"], "acronym": self.data["acronym"]}

    @classmethod
    def list_dicts(cls, query={}):
        final_data = list()
        data = cls._collection.find(query)
        for i in data:
            final_data.append({
                "name": i["name"],
                "acronym": i["acronym"]
            })
        return final_data
