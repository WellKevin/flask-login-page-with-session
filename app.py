from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    if session.get('username') is not None:
        return render_template('member.html')
    return render_template('signin.html')


@app.route("/auth", methods=['POST'])
def auth():
    acctName = request.values['acctName']
    pwd = request.values['pwd']

    if str.upper(acctName) == "TEST" and str.upper(pwd) == "TEST":
        session['username'] = acctName
        return render_template('member.html')
    return render_template('error.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.run(host='127.0.0.1', port='3000', debug=True)
