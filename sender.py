# Coded by Barlan. 2015
from tkinter import *
from tkinter.messagebox import showinfo, showerror
import smtplib

class Login(Tk):
	'''Here the Login window appears and receives data from:
		- Email account.
		- Password.
		Furthermore, tries to log in to your gmail account.'''
	def __init__(self):
		try:
			self.gmail = smtplib.SMTP("smtp.gmail.com", 587)
		except Exception as e:
			showerror("Fatal Error", str(e))
			exit()
		Tk.__init__(self)
		#self.geometry("268x157")
		self.resizable(0,0)
		self.title("e-Sender")
		self.config(bg="black")
		
		me = StringVar()
		mp = StringVar()
		Label(self, text="Your Gmail account:", bg="black", fg="green").grid(row = 0, column = 0, sticky=W)
		self.my_email = Entry(self, textvariable=me, width = 25)
		self.my_email.grid(row = 0, column = 1)

		Label(self, text="Your Password:", bg="black", fg="green").grid(row = 1, column = 0, sticky=W)
		self.my_passw = Entry(self, textvariable=mp, width = 25)
		self.my_passw.grid(row = 1, column = 1)

		self.email_button = Button(self, text="Enter", command=self.login_gmail, bg="black", fg="green")
		self.email_button.grid(row = 2, column = 0, sticky=NSEW)

		salir = Button(self, text="Exit", command=self.quit, bg="black", fg="red")
		salir.grid(row = 2, column = 1, sticky=NSEW)

	def login_gmail(self):
		account = self.my_email.get()
		self.password = self.my_passw.get()
		self.gmail.ehlo()
		self.gmail.starttls()
		try:
			self.gmail.login(account, self.password)
			showinfo("Success", "You are now logged in Gmail.")
		except:
			showerror("Error", "Unable to login into %s." % account)
			exit()
		gmail = self.gmail
		newEmail(gmail, account)
		self.withdraw()

class newEmail(Login):
	''' Now we can create a new email, specifying:
			- to
			- subject
			- message'''
	def __init__(self, gmail, account):
		Tk.__init__(self)
		self.wm_iconbitmap("icono.ico")
		self.resizable(0,0)
		self.title("New Email")
		self.config(bg="black")
		self.gmail = gmail
		self.email = account

		et = StringVar()
		es = StringVar()
		Label(self, text="From: %s" % account, bg="black", fg="orange").grid(row=0, column=0, sticky=NSEW)

		Label(self, text="To:", bg="black", fg="green").grid(row = 1, column = 0, sticky=W)
		self.email_to = Entry(self, textvariable=et, width = 25)
		self.email_to.grid(row = 1, column = 1, sticky=E)

		Label(self, text="Subject:", bg="black", fg="green").grid(row = 2, column = 0, sticky=W)
		self.email_subject = Entry(self, textvariable=es, width = 25)
		self.email_subject.grid(row = 2, column = 1, sticky=E)

		Label(self, text="Your Message:", bg="black", fg="green").grid(row = 3, column = 0, sticky=W)
		self.email_msg = Text(self, width = 25, height = 5)
		self.email_msg.grid(row = 3, column = 1, sticky=E)

		self.email_button = Button(self, text="Send", command=self.sendEmail, bg="black", fg="green")
		self.email_button.grid(row = 4, column = 0, sticky=NSEW)

		salir = Button(self, text="Exit", command=self.quit, bg="black", fg="red")
		salir.grid(row = 4, column = 1, sticky=NSEW)

	def sendEmail(self):
		self.to = self.email_to.get()
		self.subject = self.email_subject.get()
		self.msg = self.email_msg.get("1.0", END)
		headers = "From: %s\nTo: %s\nSubject: %s\n\n" % (self.email, self.to, self.subject)
		body = str(headers + self.msg)
		try:
			self.gmail.sendmail(self.email, self.to, body)
			showinfo("Completed","Email sent successfully to %s" % self.to)
			exit()
		except Exception as e:
			showerror("Error", str(e))
			exit()

L = Login()
L.mainloop()
