from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
import io
import tempfile

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def removerFundo():
    if 'file' not in request.files:
        return "Nenhum arquivo foi enviado."

    file = request.files['file']

    if file.filename == '':
        return "Nenhum arquivo selecionado."

    input_img = Image.open(file)
    output_img = remove(input_img)
    
    output_bytes = io.BytesIO()
    output_img.save(output_bytes, format='PNG')
    output_bytes.seek(0)

    # Salvar os bytes em um arquivo temporário
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    temp_file.write(output_bytes.getvalue())
    temp_file.close()

    # Enviar o arquivo temporário como um anexo para download
    return send_file(
        temp_file.name,
        mimetype='image/png',
        as_attachment=True,
        download_name= file.filename + '.png'  # Especifica o nome do arquivo para download
    )

if __name__ == '__main__':
    app.run(debug=True)
