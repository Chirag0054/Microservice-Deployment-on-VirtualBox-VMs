  from flask import Flask
  app = Flask(__name__)

  @app.route('/')
  def home():
      return ‘VCC Assigment 1 done’

  if __name__ == '__main__':
      app.run(host='0.0.0.0', port=6000)
