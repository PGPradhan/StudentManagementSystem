from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import mysql.connector
from mysql.connector import Error
import re


def f1():
	root.withdraw()
	falog.deiconify()
def f2():
	falog.withdraw()
	root.deiconify()
def f3():
	root.withdraw()
	stlog.deiconify()
def f4():
	stlog.withdraw()
	root.deiconify()
def f5():


	con=None
	try:
		con = mysql.connector.connect(host='localhost',
                                         database='student',
                                         user='root',
                                         password='7506695675')
		cursor=con.cursor()
		un=entfaUsername.get()
		pas=entfaPassword.get()
		sql="select * from facultylogin where username='%s' and password='%s'"
		args=(un,pas)
		cursor.execute(sql % args)
		c=cursor.fetchone()
		if c==None:
			msg="Invalid login info"
			messagebox.showinfo("Wrong",msg)
			entfaUsername.delete(0,END)
			entfaUsername.focus()
			entfaPassword.delete(0,END)
			entfaPassword.focus()
			

		else:
			entfaUsername.delete(0,END)
			entfaUsername.focus()
			entfaPassword.delete(0,END)
			entfaPassword.focus()
			falog.withdraw()
			fapage.deiconify()
	
	except  Error as e:
		con.rollback()
		messagebox.showinfo("Invalid username or passsword,try again",e)
	finally:
		if con is not None:
			con.close()

def f6():
	fapage.withdraw()
	falog.deiconify()
def f7():
	fapage.withdraw()
	adstmks.deiconify()
def f8():
	adstmks.withdraw()
	fapage.deiconify()
def f9():
	fapage.withdraw()
	upstmks.deiconify()
def f10():
	upstmks.withdraw()
	fapage.deiconify()

def f11():
	stdata.delete(1.0,END)
	dispgrade.delete(1.0,END)
	fapage.withdraw()
	vist.deiconify()
	con=None
	try:
		con = mysql.connector.connect(host='localhost',
                                         database='student',
                                         user='root',
                                         password='7506695675')
		print("Connected")
		sql="select * from studentmarks Order by rno"
		cursor=con.cursor()
		cursor.execute(sql)
		data=cursor.fetchall()
		msg=""
		heading="RNO     ENGLISH    MATHS     SCIENCE    TOTAL    PERCENTAGE\n" 
		stdata.insert(INSERT,heading)
		for d in data:

			msg=msg=msg+"" + str(d[0]) + "        "+str(d[1]) + "        "+str(d[2])+ "         "+str(d[3])+ "         "+str(d[4])+ "         "+str(d[5])+"\n"
		stdata.insert(INSERT,msg)
		passc="PASSED STUDENTS "
		dispgrade.insert(INSERT,passc)
		cursor.callproc('passcount')
		for result in cursor.stored_results():
			p=result.fetchall()
		for f in p:
			msg1=" "+str(f[0])
		dispgrade.insert(INSERT,msg1)
		failc="\nFAILED STUDENTS "
		dispgrade.insert(INSERT,failc)
		cursor.callproc('failcount')
		for result in cursor.stored_results():
			p=result.fetchall()
		for f in p:
			msg2=" "+str(f[0])
		dispgrade.insert(INSERT,msg2)



	
	except Error as e:
		messagebox.showerror("Galat kiya",e)

	finally:
		if con is not None:
			con.close()
			print("disconnected")
	
def f12():
	vist.withdraw()
	fapage.deiconify()
def f13():
	con=None
	try:
		con = mysql.connector.connect(host='localhost',
                                         database='student',
                                         user='root',
                                         password='7506695675')
		cursor=con.cursor()
		un=entstUsername.get()
		pas=entstPassword.get()
		patrno=re.match('^[0-9 ]+$',un)
		if (un.isalpha() or not patrno or int(un) < 1):
			messagebox.showerror("Invalid Rno","Invalid rno entered")
			entstUsername.delete(0,END)
			entstUsername.focus()
		else:
			un=int(un)
			sql="select * from studentlogin where rno='%d' and password='%s'"
			args=(un,pas)
			cursor.execute(sql % args)
			c=cursor.fetchone()
			if c==None:
				msg="Invalid login info"
				messagebox.showinfo("Wrong",msg)
				entstUsername.delete(0,END)
				entstUsername.focus()
				entstPassword.delete(0,END)
				entstPassword.focus()
			

			else:
				entstUsername.delete(0,END)
				entstUsername.focus()
				entstPassword.delete(0,END)
				entstPassword.focus()
				stmarks.delete(1.0,END)
				stlog.withdraw()
				stpage.deiconify()	
				msg=""
				heading="RNO     ENGLISH    MATHS     SCIENCE    TOTAL    PERCENTAGE" 
				stmarks.insert(INSERT,heading)
				cursor.callproc('seeresult',[un,])

				for result in cursor.stored_results():
					data=result.fetchall()
				
				for d in data:
					msg=msg=msg+"" + str(d[0]) + "        "+str(d[1]) + "        "+str(d[2])+ "         "+str(d[3])+ "         "+str(d[4])+ "        "+str(d[5])+"\n"
				stmarks.insert(INSERT,msg)
				yourgrade="\nRESULT"
				stmarks.insert(INSERT,yourgrade)
				cursor.callproc('passorfail',[un,])

				for result in cursor.stored_results():
					g=result.fetchall()
				for f in g:
					msg1="\n"+str(f[0])
				stmarks.insert(INSERT,msg1)

								

	except  Error as e:
		con.rollback()
		messagebox.showinfo("Invalid username or passsword,try again",e)
	finally:
		if con is not None:
			con.close()

	
def f14():
	
	stpage.withdraw()
	stlog.deiconify()
	

def f15():
	con=None
	try:
		con = mysql.connector.connect(host='localhost',
                                         database='student',
                                         user='root',
                                         password='7506695675')
		cursor=con.cursor()
		rno=entAddRno.get()
		eng=entEnglish.get()
		sci=entScience.get()
		maths=entMaths.get()
		patrno=re.match('^[0-9 ]+$',rno)
		pateng=re.match('^[0-9 ]+$',eng)
		patsci=re.match('^[0-9 ]+$',sci)
		patmath=re.match('^[0-9 ]+$',maths)

		if (rno.isalpha() or not patrno or int(rno) < 1 ):
			messagebox.showerror("Invalid Rno","Invalid rno entered")
			entAddRno.delete(0,END)
			entAddRno.focus()
		elif (eng.isalpha() or not pateng or int(eng)<0) or (int(eng)>100 ):
			messagebox.showerror("Invalid Marks","Invaild english marks entered")
			entEnglish.delete(0,END)
			entEnglish.focus()
		elif (maths.isalpha() or not patmath or int(maths)<0) or (int(maths)>100 ):
			messagebox.showerror("Invalid Marks","Invaild maths marks entered")
			entMaths.delete(0,END)
			entMaths.focus()
		elif (sci.isalpha() or not patsci or int(sci)<0) or (int(sci)>100 ):
			messagebox.showerror("Invalid Marks","Invaild science marks entered")
			entScience.delete(0,END)
			entScience.focus()	
		else:
			rno=int(rno)
			eng=int(eng)
			maths=int(maths)
			sci=int(sci)


			sql="insert into studentmarks values('%d', '%d','%d','%d',0,0)"
			args=(rno,eng,maths,sci)
			cursor.execute(sql % args)
			con.commit()
			msg=str(cursor.rowcount)+"records inserted"
			messagebox.showinfo("Sahi kiya",msg)
			entEnglish.delete(0,END)
			entAddRno.delete(0,END)
			entMaths.delete(0,END)
			entScience.delete(0,END)
			entAddRno.focus()
			entEnglish.focus()
			entScience.focus()
			entMaths.focus()
	except  Error as e:
		con.rollback()
		messagebox.showinfo("Galat kiya",e)
	finally:
		if con is not None:
			con.close()

def f16():
	con=None
	try:
		

		con = mysql.connector.connect(host='localhost',
                                         database='student',
                                         user='root',
                                         password='7506695675')
		cursor=con.cursor()
		rno=entupRno.get()
		eng=entupEnglish.get()
		sci=entupScience.get()
		maths=entupMaths.get()
		patrno=re.match('^[0-9 ]+$',rno)
		pateng=re.match('^[0-9 ]+$',eng)
		patsci=re.match('^[0-9 ]+$',sci)
		patmath=re.match('^[0-9 ]+$',maths)

		if (rno.isalpha() or not patrno or int(rno) < 1 ):
			messagebox.showerror("Invalid Rno","Invalid rno entered")
			entupRno.delete(0,END)
			entupRno.focus()
		elif (eng.isalpha() or not pateng or int(eng)<0) or (int(eng)>100 ):
			messagebox.showerror("Invalid Marks","Invaild english marks entered")
			entupEnglish.delete(0,END)
			entupEnglish.focus()
		elif (maths.isalpha() or not patmath or int(maths)<0) or (int(maths)>100 ):
			messagebox.showerror("Invalid Marks","Invaild maths marks entered")
			entupMaths.delete(0,END)
			entupMaths.focus()
		elif (sci.isalpha() or not patsci or int(sci)<0) or (int(sci)>100 ):
			messagebox.showerror("Invalid Marks","Invaild science marks entered")
			entupScience.delete(0,END)
			entupScience.focus()	
		else:
			rno=int(rno)
			eng=int(eng)
			maths=int(maths)
			sci=int(sci)


			sql="update studentmarks set english='%d',maths='%d',science='%d' where rno='%d'"
			args=(eng,maths,sci,rno)
			cursor.execute(sql % args)
			con.commit()
			msg=str(cursor.rowcount)+"records updated "
			messagebox.showinfo("Sahi kiya",msg)
			entupEnglish.delete(0,END)
			entupRno.delete(0,END)
			entupMaths.delete(0,END)
			entupScience.delete(0,END)
			entupRno.focus()
			entupEnglish.focus()
			entupScience.focus()
			entupMaths.focus()
	except  Error as e:
		con.rollback()
		messagebox.showinfo("Galat kiya",e)
	finally:
		if con is not None:
			con.close()


def f17():
	stlog.withdraw()
	chpass.deiconify()
	
def f18():
	chpass.withdraw()
	stlog.deiconify()
	
def f19():
	con=None
	try:
		

		con = mysql.connector.connect(host='localhost',
                                         database='student',
                                         user='root',
                                         password='7506695675')
		cursor=con.cursor()
		rno=entchpassrno.get()
		prevpass=entprevpass.get()
		newpass=entnewpass.get()
		chrno=re.match('^[0-9 ]+$',rno)

		if (rno.isalpha() or not chrno or int(rno) < 1 ):
			messagebox.showerror("Invalid Rno","Invalid rno entered")
			entchpassrno.delete(0,END)
			entchpassrno.focus()
		
		else:
			rno=int(rno)
			sql="select * from studentlogin where rno='%d' and password='%s'"
			args=(rno,prevpass)
			cursor.execute(sql % args)
			c=cursor.fetchone()
			if c==None:
				msg="Invalid rno or password entered"
				messagebox.showinfo("Wrong",msg)
				entstUsername.delete(0,END)
				entchpassrno.delete(0,END)
				entnewpass.delete(0,END)
				entprevpass.delete(0,END)
			
				entchpassrno.focus()
				entnewpass.focus()
				entprevpass.focus()

			else:
				sql="update studentlogin set password='%s' where rno='%d' and password='%s'"
				args=(newpass,rno,prevpass)
				cursor.execute(sql % args)
				con.commit()
				msg=str(cursor.rowcount)+"records updated "
				messagebox.showinfo("Sahi kiya",msg)
				entchpassrno.delete(0,END)
				entnewpass.delete(0,END)
				entprevpass.delete(0,END)
			
				entchpassrno.focus()
				entnewpass.focus()
				entprevpass.focus()
			
	except  Error as e:
		con.rollback()
		messagebox.showinfo("Galat kiya",e)
	finally:
		if con is not None:
			con.close()


root=Tk()
root.title("Grading System")
root.geometry("400x400+200+70")
btnFaculty=Button(root,text="Faculty",width=10,font=("arial",20,'bold'),command=f1)
btnStudent=Button(root,text="Student",width=10,font=("arial",20,'bold'),command=f3)
btnFaculty.pack(pady=20)
btnStudent.pack(pady=20)

#faculty login
falog=Toplevel(root)
falog.title("Faculty Login")
falog.geometry("500x500+300+100")
falog.withdraw()
lblfalog=Label(falog,text="Faculty Login",font=('arial',18,'bold'))
lblfaUsername=Label(falog,text="Username",font=('arial',18,'bold'))
entfaUsername=Entry(falog,bd=2,font=('arial',18,'bold'))
lblfaPassword=Label(falog,text="Password",font=('arial',18,'bold'))
entfaPassword=Entry(falog,show="*",bd=2,font=('arial',18,'bold'))
btnfaLogin=Button(falog,text="Login",font=('arial',18,'bold'),command=f5)
btnAddBack=Button(falog,text="Back",font=('arial',18,'bold'),command=f2)
lblfalog.pack(pady=5)
lblfaUsername.pack(pady=5)
entfaUsername.pack(pady=5)
lblfaPassword.pack(pady=5)
entfaPassword.pack(pady=5)
btnfaLogin.pack(pady=5)
btnAddBack.pack(pady=5)

#Student login
stlog=Toplevel(root)
stlog.title("Student Login")
stlog.geometry("500x500+300+100")
stlog.withdraw()
lblstlog=Label(stlog,text="Student Login",font=('arial',18,'bold'))
lblstUsername=Label(stlog,text="Roll No",font=('arial',18,'bold'))
entstUsername=Entry(stlog,bd=2,font=('arial',18,'bold'))
lblstPassword=Label(stlog,text="Password",font=('arial',18,'bold'))
entstPassword=Entry(stlog,bd=2,show="*",font=('arial',18,'bold'))
btnstLogin=Button(stlog,text="Login",font=('arial',18,'bold'),command=f13)
btnAddBack=Button(stlog,text="Back",font=('arial',18,'bold'),command=f4)
btnAddChangepass=Button(stlog,text="Change Password",font=('arial',18,'bold'),command=f17) #
lblstlog.pack(pady=5)
lblstUsername.pack(pady=5)
entstUsername.pack(pady=5)
lblstPassword.pack(pady=5)
entstPassword.pack(pady=5)
btnstLogin.pack(pady=5)
btnAddChangepass.pack(pady=5)
btnAddBack.pack(pady=5)

#faculty page
fapage=Toplevel(root)
fapage.title("Faculty")
fapage.geometry("500x500+300+100")
fapage.withdraw()
btnAdd=Button(fapage,text="Add Record",width=10,font=("arial",20,'bold'),command=f7)
btnView=Button(fapage,text="View data",width=10,font=("arial",20,'bold'),command=f11)
btnUpdate=Button(fapage,text="Update data",width=10,font=("arial",20,'bold'),command=f9)
btnlogout=Button(fapage,text="Logout",width=10,font=("arial",20,'bold'),command=f6)
btnAdd.pack(pady=20)
btnView.pack(pady=20)
btnUpdate.pack(pady=20)
btnlogout.pack(pady=20)

#view marks
stpage=Toplevel(root)
stpage.title("Grade sheet")
stpage.geometry("500x300+300+100")
stpage.withdraw()
lblstmarks=Label(stpage,text="Grade Sheet",font=('arial',18,'bold'))
stmarks=scrolledtext.ScrolledText(stpage,width=90,height=5)
btnBack=Button(stpage,text="Back",font=('arial',18,'bold'),command=f14)
lblstmarks.pack(pady=5)
stmarks.pack(pady=5)
btnBack.pack(pady=5)






#Adding marks of new students
adstmks=Toplevel(root)
adstmks.title("Add student marks into the database")
adstmks.geometry("500x500+300+100")
adstmks.withdraw()
lblAddRno=Label(adstmks,text="Enter Roll No:",font=('arial',18,'bold'))
entAddRno=Entry(adstmks,bd=2,font=('arial',18,'bold'))
lblmarks=Label(adstmks,text="Enter Marks",font=('arial',18,'bold'))
lblEnglish=Label(adstmks,text="English-",font=('arial',18,'bold'))
entEnglish=Entry(adstmks,bd=2,font=('arial',18,'bold'))
lblScience=Label(adstmks,text="Science-",font=('arial',18,'bold'))
entScience=Entry(adstmks,bd=2,font=('arial',18,'bold'))
lblMaths=Label(adstmks,text="Maths-",font=('arial',18,'bold'))
entMaths=Entry(adstmks,bd=2,font=('arial',18,'bold'))
btnAddSave=Button(adstmks,text="Save",font=('arial',18,'bold'),command=f15)
btnAddBack=Button(adstmks,text="Back",font=('arial',18,'bold'),command=f8)

lblAddRno.pack(pady=5)
entAddRno.pack(pady=5)
lblmarks.pack(pady=5)
lblEnglish.pack(pady=5)
entEnglish.pack(pady=5)
lblMaths.pack(pady=5)
entMaths.pack(pady=5)
lblScience.pack(pady=5)
entScience.pack(pady=5)
btnAddSave.pack(pady=5)
btnAddBack.pack(pady=5)

#update marks
upstmks=Toplevel(root)
upstmks.title("Update student marks")
upstmks.geometry("500x500+300+100")
upstmks.withdraw()
lblupRno=Label(upstmks,text="Enter Roll No:",font=('arial',18,'bold'))
entupRno=Entry(upstmks,bd=2,font=('arial',18,'bold'))
lblupmarks=Label(upstmks,text="Enter new Marks",font=('arial',18,'bold'))
lblupEnglish=Label(upstmks,text="English-",font=('arial',18,'bold'))
entupEnglish=Entry(upstmks,bd=2,font=('arial',18,'bold'))
lblupScience=Label(upstmks,text="Science-",font=('arial',18,'bold'))
entupScience=Entry(upstmks,bd=2,font=('arial',18,'bold'))
lblupMaths=Label(upstmks,text="Maths-",font=('arial',18,'bold'))
entupMaths=Entry(upstmks,bd=2,font=('arial',18,'bold'))
btnupSave=Button(upstmks,text="Save",font=('arial',18,'bold'),command=f16)
btnupBack=Button(upstmks,text="Back",font=('arial',18,'bold'),command=f10)

lblupRno.pack(pady=5)
entupRno.pack(pady=5)
lblupmarks.pack(pady=5)
lblupEnglish.pack(pady=5)
entupEnglish.pack(pady=5)
lblupMaths.pack(pady=5)
entupMaths.pack(pady=5)
lblupScience.pack(pady=5)
entupScience.pack(pady=5)
btnupSave.pack(pady=5)
btnupBack.pack(pady=5)

#view marks
vist=Toplevel(root)
vist.title("View student marks")
vist.geometry("500x700+300+100")
vist.withdraw()
lblallmarks=Label(vist,text="Student Grade Sheet",font=('arial',18,'bold'))
stdata=scrolledtext.ScrolledText(vist,width=90,height=20)
dispgrade=scrolledtext.ScrolledText(vist,width=25,height=3)
btnViewBack=Button(vist,text="Back",font=('arial',18,'bold'),command=f12)
lblallmarks.pack(pady=5)
stdata.pack(pady=5)
dispgrade.pack(pady=5)
btnViewBack.pack(pady=5)

chpass=Toplevel(root)
chpass.title("Change Password Window")
chpass.geometry("500x500+300+100")
chpass.withdraw()
lblchpassrno=Label(chpass,text="Enter Roll No:",font=('arial',18,'bold'))
entchpassrno=Entry(chpass,bd=2,font=('arial',18,'bold'))
lblprevpass=Label(chpass,text="Enter Previous Password",font=('arial',18,'bold'))
entprevpass=Entry(chpass,bd=2,show="*",font=('arial',18,'bold'))
lblnewpass=Label(chpass,text="Enter New Password",font=('arial',18,'bold'))
entnewpass=Entry(chpass,bd=2,show="*",font=('arial',18,'bold'))
btnSave=Button(chpass,text="Save Changes",font=('arial',18,'bold'),command=f19)
btnChBack=Button(chpass,text="Back",font=('arial',18,'bold'),command=f18)
lblchpassrno.pack(pady=5)
entchpassrno.pack(pady=5)
lblprevpass.pack(pady=5)
entprevpass.pack(pady=5)
lblnewpass.pack(pady=5)
entnewpass.pack(pady=5)
btnSave.pack(pady=5)
btnChBack.pack(pady=5)







root.mainloop()