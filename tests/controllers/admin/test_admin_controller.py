import json
from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test, prepare_base):
    user = UserModel(
        {
            "name": "batata",
            "level": "admin",
            "token": "token_super_secreto_1"
        }
    ).save()
    history = HistoryModel({
        "text_to_translate": "Hello, I like videogame",
        "translate_from": "en",
        "translate_to": "ru",
    }).save()

    assert len(json.loads(HistoryModel.list_as_json())) == 1

    app_test.delete(
        f"/admin/history/{history.data['_id']}",
        headers={
            "Authorization": user.data["token"],
            "User": "batata",
        },
    )
    assert len(json.loads(HistoryModel.list_as_json())) == 0
