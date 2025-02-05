from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
  return 'Hello, World!'

if __name__ == '__main__':
  print('Server starting on http://0.0.0.0:3000')
  app.run(host='0.0.0.0', debug=True)
