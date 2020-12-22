import os
from flask import Flask, render_template, request, send_from_directory

from src.utils.auto_eraser import main as auto_eraser
from src.utils.sound_rec import main as sound_rec
from src.utils.make_fourier import main as make_fourier

app = Flask(__name__, template_folder='src/templates')


@app.route('/')
def index():
    auto_eraser()
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def recbutton():
    if request.method == 'POST':
        dt_txt = sound_rec()
        make_fourier(dt_txt)
        path = 'image/' + dt_txt + '.png'
        return render_template('result.html', dt_txt=dt_txt, path=path)
    else:
        return render_template('index.html')


@app.route('/result/<dt_txt>')
def playbutton(dt_txt):
    file = dt_txt + '.wav'
    return send_from_directory('src/static/data', file)


def main():
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
