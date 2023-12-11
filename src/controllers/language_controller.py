from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel


language_controller = Blueprint("language_controller", __name__)


@language_controller.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        initial = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")
        translate = GoogleTranslator(
            source=translate_from, target=translate_to
        ).translate(initial)

        translate_data = {
            "languages": LanguageModel.list_dicts(),
            "text_to_translate": initial,
            "translate_from": translate_from,
            "translate_to": translate_to,
            "translated": translate,
        }
    else:
        translate_data = {
            "languages": LanguageModel.list_dicts(),
            "text_to_translate": "O que deseja traduzir?",
            "translate_from": "pt",
            "translate_to": "en",
            "translated": "What do you want to translate?",
        }

    return render_template("index.html", **translate_data)


@language_controller.route("/reverse", methods=["POST"])
def reverse_post():
    initial_to_reverse = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-to")
    translate_to = request.form.get("translate-from")

    translate = GoogleTranslator(
           source=translate_to, target=translate_from
        ).translate(initial_to_reverse)

    translate_data = {
        "languages": LanguageModel.list_dicts(),
        "text_to_translate": translate,
        "translate_from": translate_from,
        "translate_to": translate_to,
        "translated": initial_to_reverse,
        }
    return render_template("index.html", **translate_data)
