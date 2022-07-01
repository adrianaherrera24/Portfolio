import csv
from crypt import methods
from flask import Flask,render_template, request, redirect # render template allow to send the html file

app = Flask(__name__)
print(__name__)

# @app.route("/<username>/<int:post_id>") # Everytime that call the root path wil execute the hello_world function
# def main(username = None, post_id = None): # username will come fron the URL as a parameters and it's passed to the html page
#     return render_template('index.html',name = username, post_id = post_id) # The render template function will look for the files in a folder that should be named as "templates"

@app.route("/") 
def home():
    return render_template('index.html')

@app.route("/index.html") 
def returnhome():
    return render_template('index.html')

@app.route("/works.html") 
def works():
    return render_template('works.html')

@app.route("/work.html") 
def work():
    return render_template('work.html')

@app.route("/<string:page>") 
def html_page(page):
    return render_template(page)

# Save the data in the database
def write_to_file(data):
    with open('database.txt','a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('db.csv','a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

# To get data from user input
@app.route('/submit_form', methods = ['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            print("Did not save to database")
    return "Not Submitted"
