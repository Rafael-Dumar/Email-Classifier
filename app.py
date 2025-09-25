from flask import Flask, jsonify, request, render_template
from principal import clean_text, classify_text, generate_response
import fitz

app = Flask(__name__)

allowed_extensions = {'txt', 'pdf'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar_email():
    try:
        email_text = ""
        file = request.files.get('file')

        # primeiro tenta o arquivo se não der tenta o texto.
        if file and file.filename != '' and allowed_file(file.filename):
            print("Processando arquivo...")
            if file.filename.lower().endswith('.txt'):
                email_text = file.read().decode('utf-8')
            elif file.filename.lower().endswith('.pdf'):
                with fitz.open(stream=file.read(), filetype="pdf") as doc:
                    for page in doc:
                        email_text += page.get_text()
        else:
            # Se não houver um arquivo válido, pega o texto do campo do formulário
            print("Processando texto da textarea...")
            email_text = request.form.get('email_text', '')

        if not email_text.strip():
            return jsonify({'error': 'Nenhum texto ou arquivo válido foi enviado.'}), 400

        cleaned_text = clean_text(email_text)
        category = classify_text(cleaned_text)
        response = generate_response(category)

        return jsonify({'category': category.capitalize(), 'response': response})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 

