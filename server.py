from flask import Flask, render_template, jsonify, request, session, redirect, url_for, escape
from data import queries

app = Flask('hunilink-server')

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def welcome_page():
    if 'email' in session:
        return render_template('welcome_page.html', email=escape(session['email']), user_status='Bejelentkezve, mint ' + session['name'])
    return render_template('welcome_page.html', user_status='Nem vagy bejelentkezve')


@app.route('/api/registration', methods=['POST'])
def api_reg():
    if request.method == 'POST':
        user_name = request.json['name']
        user_email = request.json['email']
        user_uni = request.json['uni']
        user_course = request.json['course']
        user_starting_date = request.json['starting_date']
        user_password = request.json['password']
        queries.insert_user_data(user_name, user_email, user_password, user_uni, user_course, int(user_starting_date))


@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/login')
def login(login_status=None):
    return render_template('login.html', login_status=login_status)


@app.route('/logout')
def logout():
    all_session_data = [key for key in session.keys()]
    for key in all_session_data:
        session.pop(key, None)
    return redirect(url_for('welcome_page'))


@app.route('/login-data', methods=['GET', 'POST'])
def login_data():
    if request.method == 'POST':
        user_data = queries.get_user_data(request.form['email'], request.form['password'])
        print(user_data)
        if len(user_data) == 0:
            return login(login_status='Valami nem stimmel, próbáld újra.')
        else:
            name = user_data[0]['name']
            session['email'] = request.form['email']
            session['name'] = name
            return redirect(url_for('welcome_page', user_status='Bejelentkezve, mint: ' + name))
    return login()


@app.route('/api/universities')
def api_unis():
    universities = queries.get_unis()
    return jsonify(universities)


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/universities')
def unis():
    return render_template('universities.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
