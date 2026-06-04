from flask import Flask, request, jsonify, render_template
from fsm import Rekrutmen

app = Flask(__name__)
bot = Rekrutmen()

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/lowongan.html')
def lowongan():
    return render_template('lowongan.html')

@app.route('/tentang.html')
def tentang():
    return render_template('tentang.html')

@app.route('/kontak.html')
def kontak():
    return render_template('kontak.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    bot.proses(data['message'])
    return jsonify({"response": bot.respon})

if __name__ == '__main__':
    app.run(debug=True)