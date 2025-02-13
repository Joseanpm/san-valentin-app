from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/descargar-carta')
def descargar_carta():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'carta_san_valentin.pdf', as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render asigna el puerto automáticamente
    app.run(host="0.0.0.0", port=port, debug=False)  # Asegúrate de que debug esté en False