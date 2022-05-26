from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return 'this is get request'
    else:
        return 'this is post request'
if __name__=='__main__':
    app.run(debug=True)



if __name__ == '__main__':
    app.run()
