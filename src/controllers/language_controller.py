from flask import Blueprint, render_template, request
from models.language_model import LanguageModel


language_controller = Blueprint("language_controller", __name__)


@language_controller.route("/", methods=["GET"])
def index():
    translate_data = {
        "languages": LanguageModel.list_dicts(),
        "text_to_translate": "O que deseja traduzir?",
        "translate_from": "pt",
        "translate_to": "en",
        "translated": "What do you want to translate?",
    }

    return render_template("index.html", **translate_data)
