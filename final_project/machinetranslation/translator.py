''' Module for translating from French to English and vice versa. '''
import os
from ibm_watson import ApiException
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    ''' Translates given text from English to French. '''
    try:
        result = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        french_text = result.get('translations')[0].get('translation')
        return french_text
    except ValueError:
        return None
    except ApiException:
        return ''

def french_to_english(french_text):
    ''' Translates given text from French to English. '''
    try:
        result = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        english_text = result.get('translations')[0].get('translation')
        return english_text
    except ValueError:
        return None
    except ApiException:
        return ''
