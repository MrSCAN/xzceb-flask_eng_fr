import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
import os
load_dotenv()

apikey = os.environ.get('apikey')
url = os.environ.get('url')

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(english_text):
    if english_text is None or len(english_text) == 0:
        return "Null value"
    response = language_translator.translate(text=english_text,
    model_id='en-fr').get_result()
    french_text = json.loads(json.dumps(response))["translations"][0]["translation"]
    return french_text

def frenchToEnglish(french_text):
    if french_text is None or len(french_text) == 0:
        return "Null value"
    response = language_translator.translate(text=french_text,
    model_id='fr-en').get_result()
    english_text = json.loads(json.dumps(response))["translations"][0]["translation"]
    return english_text
