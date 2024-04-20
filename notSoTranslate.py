from flask import Flask, request, jsonify
from translate import Translator

app = Flask(__name__)

def translatorFunction(text, targetLanguage):
    try:
        translator = Translator(to_lang=targetLanguage)
        translated_text = translator.translate(text)
        return translated_text

    except Exception as e:
        print(f"Translation failed: {e}")
        return None

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.get_json()
        textToTranslate = data['text']
        target_language = data['target_language']
        translated_text = translatorFunction(textToTranslate, target_language)

        if translated_text:
            return jsonify({'translated_text': translated_text}), 200
        else:
            return jsonify({'error': 'Translation failed'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
