import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('gu5st95DMdxQa54ju1mI05P50Hqi5h1Ngf_e_xPNn0Gs')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/e807a60d-067f-4bb1-b362-ae0572f0cbe3')

def english_to_french(english_text):
    """
    This function returns text in french that was converted from english
    """
    translation = language_translator.translate(english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation'] 
    return french_text

def french_to_english(french_text):
    """
    This function returns text in english that was converted from french
    """
    translation = language_translator.translate(french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text