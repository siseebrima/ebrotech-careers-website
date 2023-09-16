from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': '1',
        'title': 'Software Engineer',
        'location': 'London, UK',
        'salary': '£50,000 - £70,000',
    },
    {
        'id': '2',
        'title': 'Product Manager',
        'location': 'Liverpool, UK',
        'salary': '£50,000 - £90,000',
    },
    {
        'id': '3',
        'title': 'Sales Manager',
        'location': 'Manchester, UK',
        'salary': '£40,000 - £60,000',
    },
    {
        'id': '4',
        'title': 'Customer Success Manager',
        'location': 'Paris, France',
        'salary': '€50,000 - €70,000',
    },
    {
        'id': '5',
        'title': 'Marketing Manager',
        'location': 'Berlin, Germany',
        'salary': '€50,000 - €70,000',
    },
    {
        'id': '6',
        'title': 'Accountant',
        'location': 'San Francisco, USA',
        'salary': '$90,000 - $120,000',
    },


]


@app.route('/')
def hello_world():
    return render_template('home.html',
                           jobs=JOBS, company_name='ebrotech')


@app.route('/api/jobs')
def jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
