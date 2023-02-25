from flask import Flask,render_template
from flask import request


app = Flask(__name__,template_folder='./')
fname =""
lname=""
emailad=""

@app.route('/')
def hello():
    return render_template("userdetails.html",msg="")
    
@app.route('/login/', methods=['POST'])
def login():
        fn=""
        ln=""
        email=""
        if request.method == 'POST' and 'FirstName' in request.form and 'LastName' in request.form and 'EmailAddress' in request.form:
                firstname = request.form['FirstName']
                global fname
                fname = request.form['FirstName']
                lastname = request.form['LastName']
                global lname
                lname = request.form['LastName']
                emailaddress = request.form['EmailAddress']
                global emailad
                emailad = request.form['EmailAddress']
                
                if firstname == '' or lastname == '' or emailaddress == '':
                        msg = "Some of the entries are missing. Please enter all the details"
                        return render_template('./userdetails.html',msg=msg)
                else:
                    return render_template('./selectoptions.html',fn=firstname,ln=lastname,email=emailaddress)
        else:
            msg = "Some error with the form. Try again or contact the developer"
            return render_template('./userdetails.html',msg=msg)


@app.route('/endchat/')
def endchat():
    return render_template('./endchat.html',fn=fname,ln=lname,emailad=emailad)
   
@app.route('/questions/')
def questions():
    return render_template('./selectoptions.html')
        
@app.route('/q1/', methods=['POST'])
def q1():
    msg = "Yes, our college has both men's and women's football teams. It's great to see that our college is providing opportunities for both male and female students to participate in sports and represent the college on the field. Football is a popular sport that not only promotes physical fitness but also helps in building teamwork, discipline, and leadership skills. It's great to see that our college recognizes the importance of sports in the overall development of students and provides them with the necessary resources to excel in their athletic pursuits."
    return render_template('./response.html',msg=msg)

@app.route('/q2/', methods=['POST'])
def q2():
    msg = "Yes, our college does offer a Computer Science major. This is a great opportunity for students interested in computer technology and software development to gain valuable knowledge and skills in this field. Computer Science is a rapidly growing industry, and graduates with a degree in this major have a wide range of career options available to them, including software development, data analysis, cybersecurity, and much more. Our college recognizes the importance of preparing students for the ever-evolving field of technology and provides them with the necessary resources and training to excel in their academic and professional pursuits."
    return render_template('./response.html',msg=msg)

@app.route('/q3/', methods=['POST'])
def q3():
    msg = "The instate tuition fees for the students as of this academic year is $4500."
    return render_template('./response.html',msg=msg)
    
@app.route('/q4/', methods=['POST'])
def q4():
    msg = "Yes, our college does have on-campus housing. This provides students with the convenience of living on-campus and being closer to their classes, campus events, and resources. Living on-campus can also enhance the college experience and help students develop stronger relationships with their peers."
    return render_template('./response.html',msg=msg)
    

        


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]
