from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notal Oficial</title>
</head>
<body>
    <audio src="msc.mp3" autoplay></audio><img src="teste2.png" alt="">
</body>
</html>"""


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)