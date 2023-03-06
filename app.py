from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        output_path = request.form['output_path']

        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            if output_path:
                stream.download(output_path=output_path)
            else:
                stream.download()
            return redirect(url_for('success'))
        except:
            return render_template('index.html', error="Invalid YouTube URL")
    else:
        return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5005)
