from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to DockerDetect, say /hello to me!'


@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'Guest')
    template = f'Hello, {name}!'
    return render_template_string(template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
