from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    output_path = request.form['output_path']

    if not os.path.exists(output_path):
        return "Output path does not exist!"

    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        filesize = video.filesize
        filename = video.default_filename
        filepath = os.path.join(output_path, filename)

        # video.register_on_progress_callback(show_progress_bar)
        video.on_progress_callback = show_progress_bar

        video.download(output_path)
        return render_template('success.html', filename=filename)
    except Exception as e:
        return str(e)

def show_progress_bar(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_complete = bytes_downloaded / total_size * 100

    print(f"{percent_complete:.2f}% downloaded")
    return render_template('progress.html', percent_complete=percent_complete)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)
