from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def birthday_card():
    return render_template('birthday_card.html', name='[Name]')

if __name__ == '__main__':
    app.run()
