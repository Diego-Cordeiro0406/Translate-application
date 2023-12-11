import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history(prepare_base):
    history = json.loads(HistoryModel.list_as_json())
    assert history == [
        {
            "_id": history[0]["_id"],
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "_id": history[1]["_id"],
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        },
    ]
