from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('Home.html')

if __name__ == '__main__':
  print('Server starting on http://0.0.0.0:3000')
  app.run(host='0.0.0.0', debug=True)
