from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')


etape_active = 0


@app.route('/')
def hello_world():
    global etape_active
    titre = "Overlay Twitch"
    etapes = ["Q/A", "2", "3", "4"]
    return render_template('index.html', titre=titre , etapes = etapes, etape_active = etape_active)

@app.route('/up')
def up():
    global etape_active
    etape_active += 1
    return "up"

@app.route('/down')
def down():
    global etape_active
    etape_active -= 1
    return "down"



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5002,debug=True)
