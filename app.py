from flask import Flask, request, jsonify, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/<name>/<int:age>')
def main(name, age):
    return 'Hello %s and my age is %s' % (name, age) , 200

@app.route('/request', methods=['POST'])
def request_data():
    print(request.form['age'])
    person = request.args.get('person')
    return request.form

@app.route('/response', methods=['POST'])
def response_data():
    obj = {
        'name' : request.form['name'],
        'age': request.form['age'], 
        'github': 'github.com/krawler'
    }

    resp = make_response(jsonify(data = obj), 201)
    resp.headers['couse-powered-By'] = 'Rafael - Scool of Net'

    return resp
    #return jsonify(user = obj), 201

@app.route('/redirect', methods=['GET'])
def redirect():
    obj = {
        'name' : request.form['name'],
        'age': request.form['age'], 
        'github': 'github.com/krawler'
    }

    return redirect('/redirected', 302)


#app.add_url_rule('/', 'main')

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=8000, debug=True)