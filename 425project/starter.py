import os
from flask import Flask,redirect,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Khokhar_123@localhost/UniDB-HW4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Student_T(db.Model):
    __tablename__ = 'student_t'
    s_id = db.Column(db.String(9), primary_key=True)
    first_name = db.Column(db.String(15))    
    last_name = db.Column(db.String(15))
    gpa = db.Column(db.Float)
    earned_credits = db.Column(db.Integer)
    major = db.Column(db.String(20))
    dob = db.Column(db.Date)
class Professor_T(db.Model):
    __tablename__ = 'professor_t'
    p_id = db.Column(db.String(9), primary_key=True)
    first_name = db.Column(db.String(15))    
    last_name = db.Column(db.String(15))
    income = db.Column(db.Integer)
    dob = db.Column(db.Date)


class Department_T(db.Model):
    __tablename__ = 'department_t'
    d_name = db.Column(db.String(20), primary_key=True)
    building = db.Column(db.String(40))

class Classroom_T(db.Model):
    __tablename__ = 'classroom_t'
    c_building = db.Column(db.String(40), primary_key=True)
    room = db.Column(db.String(6), primary_key=True)    
    tot_space = db.Column(db.Integer)

class Course_T(db.Model):
    __tablename__ = 'course_t'
    c_num = db.Column(db.String(8), primary_key=True)
    c_title = db.Column(db.String(40))
    credit_hours = db.Column(db.Integer)
    d_name = db.Column(db.String(20))

@app.route("/professor",methods=["POST","GET"])
def professor():
    if request.method == "POST":
        pId= request.form["psdid"]
        pfName= request.form["pfn"]
        plName= request.form["pln"]
        pdob = request.form["pdate"]
        pInc = request.form["inc"]
        if pId != "" :
            return redirect(url_for("ps1",PSDid=pId))
        elif pfName!="" and plName!="":
            return redirect(url_for("ps2",FN=pfName,LN=plName))
        elif pfName!="" and pInc=="":
            return redirect(url_for("ps3",FN=pfName))
        elif pfName!="" and pInc!="":
            return redirect(url_for("ps4",FN=pfName,INC=pInc))
        elif pId=="" and pfName=="" and plName=="" and pdob=="" and pInc=="":
            return render_template("professor.html")
    else: return render_template("professor.html")

@app.route("/ps4<FN>,<INC>")
def ps4(FN,INC):  
        try:
            c=0
            depart = Professor_T.query.filter_by(first_name=FN,income=INC).order_by(Professor_T.income.desc()).all()
            depat_text  = 'Following Is The Result In Response To Your Query :'
            depat_text += '<ul>'
            depat_text +='<title>Professor Query Results</title>'
            depat_text += 'Professor ID, First Name, Last Name, Income($)'
            depat_text += '<p> </p>'
            for dep in depart:
                depat_text += '<li>' + dep.p_id + ', ' + dep.first_name + ', ' +  dep.last_name +','+ str(dep.income)+'</li>'
                c +=1
            depat_text += '</ul>'
            if c==0 :
                depat_text = "No Data Found"
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
        return depat_text

@app.route("/ps3<FN>")
def ps3(FN):  
        try:
            c=0
            depart = Professor_T.query.filter_by(first_name=FN).order_by(Professor_T.income.desc()).all()
            depat_text  = 'Following Is The Result In Response To Your Query :'
            depat_text += '<ul>'
            depat_text +='<title>Professor Query Results</title>'
            depat_text += 'Professor ID, First Name, Last Name, Income($)'
            depat_text += '<p> </p>'
            for dep in depart:
                depat_text += '<li>' + dep.p_id + ' , ' + dep.first_name + ' , ' +  dep.last_name +' ,'+ str(dep.income)+'</li>'
                c +=1
            depat_text += '</ul>'
            if c==0 :
                depat_text = "No Data Found"
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
        return depat_text 
 
@app.route("/ps2<FN>,<LN>")
def ps2(FN,LN):  

        try:
            c=0
            depart = Professor_T.query.filter_by(first_name=FN,last_name=LN).order_by(Professor_T.income.desc()).all()
            depat_text  = 'Following Is The Result In Response To Your Query :'
            depat_text += '<ul>'
            depat_text +='<title>Professor Query Results</title>'
            depat_text += 'Professor ID, First Name, Last Name, Income($)'
            depat_text += '<p> </p>'
            for dep in depart:
                depat_text += '<li>' + dep.p_id + ', ' + dep.first_name + ', ' +  dep.last_name +','+ str(dep.income)+'</li>'
                c +=1
            depat_text += '</ul>'
            if c==0 :
                depat_text = "No Data Found"
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
        return depat_text
    
@app.route("/ps1<PSDid>")
def ps1(PSDid):  

        try:
            c=0
            depart = Professor_T.query.filter_by(p_id = PSDid).order_by(Professor_T.income.desc()).all()
            depat_text  = 'Following Is The Result In Response To Your Query :'
            depat_text += '<ul>'
            depat_text +='<title>Professor Query Results</title>'
            depat_text += 'Professor ID, First Name, Last Name, Income($)'
            depat_text += '<p> </p>'
            for dep in depart:
                depat_text += '<li>' + dep.p_id + ', ' + dep.first_name + ', ' +  dep.last_name +','+ str(dep.income)+'</li>'
                c +=1
            depat_text += '</ul>'
            if c==0 :
                depat_text = "No Data Found"
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
        return depat_text 
        
@app.route("/student",methods=["POST","GET"])
def student():
    if request.method == "POST":
        sId= request.form["stdid"]
        fName= request.form["fn"]
        lName= request.form["ln"]
        Gpa = request.form["gpa"]
        credss = request.form["ecds"]
        dob = request.form["date"]
        Major = request.form["mjr"]
        if sId != "" :
            return redirect(url_for("st1",stdID=sId))
        elif Gpa!="" and Major!="":
            return redirect(url_for("st2",gp=Gpa,mj=Major))
        elif credss!="" and Major!="":
            return redirect(url_for("st4",cds=credss,mj=Major))
        elif Major!="":
            return redirect(url_for("st3",mj=Major))
        elif sId == "" and fName=="" and lName=="" and Gpa==""and credss==""and dob==""and Major=="":
            return render_template("student.html")
            
    else: 
        return render_template("student.html")

@app.route("/st4<cds>,<mj>")
def st4(cds,mj):  
        try:
            c=0
            depart = Student_T.query.filter_by(earned_credits = cds,major=mj).order_by(Student_T.gpa.desc()).all()
            depat_text  = 'Following Is The Result In Response To Your Query :'
            depat_text += '<ul>'
            depat_text +='<title>Student Query Results</title>'
            depat_text += 'Student ID, First Name, GPA, Earned Credits, Major'
            depat_text += '<p> </p>'
            for dep in depart:
                depat_text += '<li>' + dep.s_id + ', ' + dep.first_name + ', ' + str(dep.gpa) +','+ str(dep.earned_credits) + ','+dep.major  +'</li>'
                c +=1
            depat_text += '</ul>'
            if c==0 :
                depat_text = "No Data Found"
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
        return depat_text 

@app.route("/st3<mj>")
def st3(mj):  

        try:
            c=0
            depart = Student_T.query.filter_by(major = mj).order_by(Student_T.gpa.desc()).all()
            depat_text = '<ul>'
            depat_text +='<title>Student Query Results</title>'
            depat_text += 'Student ID, First Name, GPA, Earned Credits, Major'
            depat_text += '<p> </p>'
            for dep in depart:
                depat_text += '<li>' + dep.s_id + ', ' + dep.first_name + ', ' + str(dep.gpa) +','+ str(dep.earned_credits) + ','+dep.major  +'</li>'
                c +=1
            depat_text += '</ul>'
            if c==0 :
                depat_text = "No Data Found"
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
        return depat_text 
@app.route("/st2<gp>,<mj>")
def st2(gp,mj):  
        try:
            c=0
            depart = Student_T.query.filter_by(gpa = gp,major=mj).order_by(Student_T.gpa.desc()).all()
            depat_text  = 'Following Is The Result In Response To Your Query :'
            depat_text += '<ul>'
            depat_text +='<title>Student Query Results</title>'
            depat_text += 'Student ID, First Name, GPA, Earned Credits, Major'
            depat_text += '<p> </p>'
            for dep in depart:
                depat_text += '<li>' + dep.s_id + ', ' + dep.first_name + ', ' + str(dep.gpa) +','+ str(dep.earned_credits) + ','+dep.major  +'</li>'
                c +=1
            depat_text += '</ul>'
            if c==0 :
                depat_text = "No Data Found"
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
        return depat_text 

@app.route("/classroom",methods=["POST","GET"])
def classroom():  
    if request.method == "POST":
        buildN= request.form["buildn"]
        rooM= request.form["room"]
        tspace= request.form["totspace"]
        if buildN != "" and tspace != "":
            return redirect(url_for("cls1",bn=buildN,tsp=tspace))
        elif buildN != "":
            return redirect(url_for("cls2",bn=buildN))
        elif buildN == "" and rooM=="" and tspace=="":
            return render_template("classroom.html")
    else: return render_template("classroom.html")
    
@app.route("/st1<stdID>")
def st1(stdID):  

        try:
            c=0
            depart = Student_T.query.filter_by(s_id = stdID).order_by(Student_T.gpa.desc()).all()
            depat_text  = 'Following Is The Result In Response To Your Query :'
            depat_text += '<ul>'
            depat_text +='<title>Student Query Results</title>'
            depat_text += 'Student ID, First Name, GPA, Earned Credits, Major'
            depat_text += '<p> </p>'
            for dep in depart:
                depat_text += '<li>' + dep.s_id + ', ' + dep.first_name + ', ' + str(dep.gpa) +','+ str(dep.earned_credits) + ','+dep.major  +'</li>'
                c +=1
            depat_text += '</ul>'
            if c==0 :
                depat_text = "No Data Found"
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
        return depat_text 
    
@app.route("/cls2<bn>")
def cls2(bn):  
        try:
            c=0
            depart = Classroom_T.query.filter_by(c_building = bn).order_by(Classroom_T.room).all()
            depat_text  = 'Following Is The Result In Response To Your Query :'
            depat_text += '<ul>'
            depat_text +='<title>ClassRoom Query Results</title>'    
            depat_text += 'Building Name, Room, Total Space'
            depat_text += '<p> </p>'
            for dep in depart:
                depat_text += '<li>' + dep.c_building + ', ' + dep.room + ', ' + str(dep.tot_space)  +'</li>'
                c +=1
            depat_text += '</ul>'
            if c==0 :
                depat_text = "No Data Found"
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
        return depat_text     
    
@app.route("/cls1<bn>,<tsp>")
def cls1(bn,tsp):  
        try:
            c=0
            depart = Classroom_T.query.filter_by(c_building = bn, tot_space = tsp).order_by(Classroom_T.room).all()
            depat_text  = 'Following Is The Result In Response To Your Query :'
            depat_text += '<ul>'
            depat_text +='<title>ClassRoom Query Results</title>'    

            depat_text += 'Building Name, Room, Total Space'
            depat_text += '<p> </p>'
            for dep in depart:
                depat_text += '<li>' + dep.c_building + ', ' + dep.room + ', ' +str(dep.tot_space)  +'</li>'
                c +=1
            depat_text += '</ul>'
            if c==0 :
                depat_text = "No Data Found"
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
        return depat_text  
    
@app.route("/course", methods=["POST","GET"])
def course():
    if request.method == "POST":
        DName= request.form["dname"]
        cNum= request.form["cnum"]
        cTitle= request.form["ctitle"]
        cHrs= request.form["chrs"]
        # if len(cHrs)> 1 :
        #     operator = cHrs[1]
        if DName != "" and cHrs!="":
            # if operator  ==">" or operator == "<":
            #     return redirect(url_for("crs2",cred=cHrs[2],op=operator))
            # else: 
            return redirect(url_for("crs1",dn=DName,cred=cHrs))
        elif cNum != "":
            return redirect(url_for("crs2",cnum =cNum))
        elif DName != "":
            return redirect(url_for("crs4",ddname=DName))
        elif DName == "" and cNum=="" and cTitle=="" and cHrs=="":
            return render_template("course.html")

    else:
        return render_template("course.html")

@app.route("/crs4<ddname>")
def crs4(ddname):  
        try:
            c=0
            depart = Course_T.query.filter_by(d_name = ddname).order_by(Course_T.c_title).all()
            depat_text  = 'Following Is The Result In Response To Your Query :'
            depat_text += '<ul>'
            depat_text +='<title>Course Query Results</title>'  
            depat_text += 'Department Name, Course Num, Course Title, Credit Hours'
            depat_text += '<p> </p>'
            for dep in depart:
                depat_text += '<li>' + dep.d_name + ', ' + dep.c_num + ', ' +dep.c_title + ', ' + str(dep.credit_hours) +'</li>'
                c +=1
            depat_text += '</ul>'
            if c==0 :
                depat_text = "No Data Found"
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
        return depat_text
@app.route("/crs2<cnum>")
def crs2(cnum):  
        try:
            c=0
            depart = Course_T.query.filter_by(c_num = cnum).order_by(Course_T.c_title).all()
            depat_text  = 'Following Is The Result In Response To Your Query :'
            depat_text += '<ul>'
            depat_text +='<title>Course Query Results</title>'  
            depat_text += 'Department Name, Course Num, Course Title, Credit Hours'
            depat_text += '<p> </p>'
            for dep in depart:
                depat_text += '<li>' + dep.d_name + ', ' + dep.c_num + ', ' +dep.c_title + ', ' + str(dep.credit_hours) +'</li>'
                c +=1
            depat_text += '</ul>'
            if c==0 :
                depat_text = "No Data Found"
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
        return depat_text  
    
@app.route("/crs1<dn>,<cred>")
def crs1(dn,cred):  
        try:
            c=0
            depart = Course_T.query.filter_by(d_name=dn,credit_hours=cred).order_by(Course_T.c_title).all()
            depat_text  = 'Following Is The Result In Response To Your Query :'
            depat_text += '<ul>'
            depat_text +='<title>Course Query Results</title>'  
            depat_text += 'Department Name, Course Num, Course Title, Credit Hours'
            depat_text += '<p> </p>'
            for dep in depart:
                depat_text += '<li>' + dep.d_name + ', ' + dep.c_num + ', ' +dep.c_title + ', ' + str(dep.credit_hours) +'</li>'
                c +=1
            depat_text += '</ul>'
            if c==0 :
                depat_text = "No Data Found"
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
        return depat_text   

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        option= request.form["optdata"]
        if option == "4":
            return redirect(url_for("dep"))
        elif option=="3":
            return redirect(url_for("course"))
        elif option=="1":
            return redirect(url_for("student"))
        elif option=="5":
            return redirect(url_for("classroom"))
        elif option=="2":
            return redirect(url_for("professor"))
        else:
            return render_template("home.html")
    else:  
        return render_template("home.html")

@app.route('/dep',methods=["POST","GET"])
def dep():
    render_template("dep.html")
    if request.method == "POST":
        dName= request.form["depname"]
        BName= request.form["buildname"]

        if dName == "" and BName=="":
            return redirect(url_for("depres3"))
        elif dName != "" and BName=="":
            return redirect(url_for("depres2",dd=dName))
        elif dName == "" and BName!="":
            return redirect(url_for("depres0",bb=BName))
        else:
            return redirect(url_for("depres",dd=dName,bb=BName))
    else:
        return render_template("dep.html")

@app.route('/depres<bb>')
def depres0(bb):  
        try:
            c=0
            depart = Department_T.query.filter_by(building=bb).order_by(Department_T.d_name).all()
            depat_text  = 'Following Is The Result In Response To Your Query :'
            depat_text += '<ul>'
            depat_text +='<title>Department Query Results</title>'  
            depat_text += 'Department Name, Builduing Name'
            depat_text += '<p> </p>'
            for dep in depart:
                depat_text += '<li>' + dep.d_name + ', ' + dep.building + '</li>'
                c +=1
            depat_text += '</ul>'
            if c==0 :
                depat_text = "No Data Found"
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
        return depat_text   

@app.route('/depres<dd>,<bb>')
def depres(dd,bb):  
        try:
            c=0
            depart = Department_T.query.filter_by(d_name=dd,building=bb).order_by(Department_T.d_name).all()
            depat_text  = 'Following Is The Result In Response To Your Query :'
            depat_text += '<ul>'
            depat_text +='<title>Department Query Results</title>'  
            depat_text += 'Department Name, Builduing Name'
            depat_text += '<p> </p>'
            for dep in depart:
                depat_text += '<li>' + dep.d_name + ', ' + dep.building + '</li>'
                c +=1
            depat_text += '</ul>'
            if c==0 :
                depat_text = "No Data Found"
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
        return depat_text

@app.route('/depres2<dd>')
def depres2(dd):  
        try:
            c=0
            depart = Department_T.query.filter_by(d_name=dd).order_by(Department_T.d_name).all()
            depat_text  = 'Following Is The Result In Response To Your Query :'
            depat_text += '<ul>'
            depat_text +='<title>Department Query Results</title>'
            depat_text += 'Department Name, Builduing Name'
            depat_text += '<p> </p>'
            for dep in depart:
                depat_text += '<li>' + dep.d_name + ', ' + dep.building + '</li>'
                c +=1
            depat_text += '</ul>'
            if c==0 :
                depat_text = "No Data Found"
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
        return depat_text

@app.route('/depres3')
def depres3():  
        try:
            c=0
            depart = Department_T.query.order_by(Department_T.d_name).all()
            depat_text  = 'Following Is The Result In Response To Your Query :'
            depat_text += '<ul>'
            depat_text +='<title>Department Query Results</title>'
            depat_text += 'Department Name, Builduing Name'
            depat_text += '<p> </p>'
            for dep in depart:
                depat_text += '<li>' + dep.d_name + ', ' + dep.building + '</li>'
                c +=1
            depat_text += '</ul>'
            if c==0 :
                depat_text = "No Data Found"
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
        return depat_text
   

# @app.route('/test') JUST A METHOD FOR TESTING 
# def index():
    
#     try:
#         c=0
#         depart = Department_T.query.filter_by(d_name="Computer Science",building="IIT Tower").order_by(Department_T.d_name).all()
#         depart_text = '<ul>'
#         for dep in depart:
#             depart_text += '<li>' + dep.d_name + ', ' + dep.building + '</li>'
#             c +=1
#         depart_text += '</ul>'
#         if c==0 :
#             depart_text = "No Data Found"
#         return depart_text
#     except Exception as e:
#         # e holds description of the error
#         error_text = "<p>The error:<br>" + str(e) + "</p>"
#         hed = '<h1>Something is broken.</h1>'
#         return hed + error_text

if __name__ == '__main__':
    app.run(debug=True)
