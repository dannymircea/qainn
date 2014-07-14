from mod_python import Cookie
from mod_python import util
import  os, sqlite3, random, time

# functions for other computations
def muaDATEo3Kw8Lbikg():
	"""
		This should get the current date
	"""
	pass


# functions for other computations
def mmfao2K98Lbkkg(specificCharSet, desiredLength):
	"""
		This should generate a auth cookie string; which should be unique per user
		TODO: not fully implemented 
			- please check if this is unique in the database, here or in another function
	"""
	generatedAuthCookie = "" # this should get overwritten

	specificCharSetLength = len(specificCharSet) - 1
	for count in range(0, desiredLength): # generate a random char from specificCharSet 
		generatedAuthCookie += specificCharSet[random.randint(0, specificCharSetLength)] 

	return generatedAuthCookie

def xvmpilomarCreate(req):
	"""
		Called when creating a new user;
		On success it should generate the directory with a proper success message
	"""

	"""
	conn = sqlite3.connect("/var/www/m/site.db")

	cur = conn.cursor()
	cur.execute("insert into newusers (usrname, imgsrc, createdate, occupation, authcookie, password, email, phone, language, gender)\
		values(req.form['usrname']+
			   req.form['passwd'] +\
			   req.form[''] +\
			   req.form[''] +\
			   req.form[''] +\
			   )")
	"""
	if req.method != "POST":
		util.redirect(req, location = '/m/hell', permanent = False, text = "Only POST accepted")	
		
	forAuthCookie = ['z', '7', 'x', 'O', 'L', 'n', 'M', 'k', 'w', 'a', '1', '3', '2']
	newUsername = req.form['usrname']
	newFulluser = req.form['fullusr']
	newPassword = req.form['passwd']
	newEmail = req.form['email']
	newPhone = req.form['phone']
	newOccup = req.form['occupation']
	newGender = req.form['gender_radio']
	newLang = req.form['langSelect']
	newImage = req.form['picturefile']
	newGenAuthCookie = mmfao2K98Lbkkg(forAuthCookie, 17)
	newCreatedate = '24-06-2014_23:40:01'

	uploadImg(newImage)
	ret = newImage.filename +" :: " +	newUsername + ":: " +	newFulluser + ":: " +	newPassword + ":: " +	newEmail + ":: " +	newPhone + ":: " +	newOccup + ":: " +	newGender + ":: " +	newLang + ":: " +	newGenAuthCookie + ":: " 

	"""
	"""

	conn = sqlite3.connect("/var/www/m/site.db")
	# conn = sqlite3.connect("/var/www/m/site.db")

	"""
	conn.execute(""INSERT INTO newusers (usrname, imgsrc, createdate, password, email)	VALUES(?, ?, ?, ?, ?);"", (newUsername,	'uidpics/'+newImage, newCreatedate, newPassword, newEmail))

	"""
	conn.execute("""INSERT INTO newusers (usrname, imgsrc, createdate, lastlogin,\
	occupation, authcookie, password, email, phone, language, gender)\
	VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", (newUsername,\
	'uidpics/'+newImage.filename, newCreatedate, 'noLoginYet', newOccup, newGenAuthCookie, newPassword,\
	newEmail, newPhone, newLang, newGender))
	conn.commit()
	conn.close()

	return generateDir(req, 'createUser')
	# return "tot:"+ ret + "-- " +os.getcwd()

	"""
	fields = "start__" +  req.form['langSelect']
	for i in util.FieldStorage(req).list:
		# fields += ":: "
		fields += ":: " + "[%s]=%s" % (i.name, i.value)
	return "form:"+fields
	"""


def generateDir(req, callfunction):
	"""
		Generates the directory page content (profile boxes) - this is a actual page
	"""
	conn = sqlite3.connect("/var/www/m/site.db")

	cur = conn.cursor()
	cur.execute("select * from newusers;")

	rows = cur.fetchall()

	directory  = "";
	# generating profile boxes
	for i in rows:
		# profBox = "<div><p>" +i[1]+ "</p></div>"
		# profBox = "<div><p>" +i[1]+ "</p></div>"
		profBox = """\
		<div id="userprofilebox" >
			<div id="profileImg">
				<img src="../../""" + i[2] + """" title=' """ +i[8]+ """ ' style="max-width:160px; max-height:160px;" >
			</div>
			<div id="profileDescription">
				<hr width=90%>
				<p>Name:&nbsp;&nbsp;&nbsp;""" + i[1] + """</p>
				<p>Occupation:&nbsp;&nbsp;""" + i[5] + """</p>
			</div>
			<div id="profileLastInfo">
				<p>Last login:&nbsp;&nbsp;&nbsp;""" + i[4] +"""</p>
			</div>
		</div>
		"""
		directory  += profBox
	
	htmlpage = """\
	<html>
	<head>
		<script src="../../soc/res/js/tstamp02072014.js"></script>
		<link rel="stylesheet" type="text/css" href="../../soc/res/css/main.css">
		<title>Smartbook</title>
	</head>
		<body>
			<div id="zaheader">
				<p> Header</p>
			</div><!-- za header end-->

			<div id="zamaincontent">
				<p> MainContent</p>
				<div id="za-maincontent-left">
					<p> MainContent-Left</p>
					""" + directory + """
				</div><!-- za za-maincontent-left end-->
				<div id="za-maincontent-right">
					<p> MainContent-Right</p>
					<div class="registration-form" >
						<form enctype="multipart/form-data" action="hell/xvmpilomarCreate" method="post">
							<label for="username_f" id="username_flbl">Username:</label>
							<input class="registration-form-input" type="text" name="usrname" id="username_f" onblur="validate(this)" onmouseover="inputColorFadeIn(this)" onmouseout="inputColorFadeOut(this)"><p id="username_ferrinf" style="display:none"></p><br/>
							<label for="fulluser_f" id="fulluser_flbl">Full name:</label>
							<input class="registration-form-input" type="text" name="fullusr" id="fulluser_f" onblur="validate(this)" onmouseover="inputColorFadeIn(this)" onmouseout="inputColorFadeOut(this)"><p id="fulluser_ferrinf" style="display:none"></p><br/>
							<label for="password_f">Password:</label>
							<input class="registration-form-input" type="password" name="passwd" id="password_f" onmouseover="inputColorFadeIn(this)" onmouseout="inputColorFadeOut(this)"><br/>
							<label for="passwordc_f">Confirm password:</label>
							<input class="registration-form-input" type="password" name="passwdc" id="passwordc_f" onmouseover="inputColorFadeIn(this)" onmouseout="inputColorFadeOut(this)"><br/>
							<label for="email_f" id="email_flbl">Email:</label>
							<input class="registration-form-input" type="text" name="email" id="email_f"  onblur="validate(this)" onmouseover="inputColorFadeIn(this)" onmouseout="inputColorFadeOut(this)"><p id="email_ferrinf" style="display:none"></p><br/>
							<label for="phone_f">Phone:</label>
							<input class="registration-form-input" type="text" name="phone" id="phone_f" onmouseover="inputColorFadeIn(this)" onmouseout="inputColorFadeOut(this)"><br/>
							<label for="occup_f">Occupation:</label>
							<input class="registration-form-input" type="text" name="occupation" id="occup_f"  onmouseover="inputColorFadeIn(this)" onmouseout="inputColorFadeOut(this)"><br/>
							<label for="female_f">female:</label>
							<input type="radio" name="gender_radio" value="female" id="female_f" >
							<label for="male_f">male:</label>
							<input type="radio" name="gender_radio" value="male" id="male_f" ></br>
							<label for="language_f">Language:</label>
							<select name="langSelect">
								<option value="notSelected">Please select</option>
								<option value="English_lang">English</option>
								<option value="French_lang">French</option>
								<option value="Romanian_lang">Romanian</option>
								<option value="German_lang">German</option>
								<option value="Italian_lang">Italian</option>
								<option value="Japanese_lang">Japnese</option>
							</select><br/>

							<input type="file" name="picturefile"  id="poza_f" ><br/>
							<input type="submit" value="Trimite username">
						</form>
					</div>
				</div><!-- za za-maincontent-right end-->

				</div><!-- za maincontent end-->
				<div id="zafooter">
					<p> Footer</p>
				</div><!-- za footer end-->

			<!--
			<h1>Welcome message from Danny </h1>
			""" + directory + """
			-->
		</body>
	</html>
	"""
	# returning page content

	if callfunction == 'createUser':
		util.redirect(req, location = '/m/hell', permanent = False, text = "Created user OK")	
	return htmlpage

# def uploadImg(req):
def uploadImg(submittedFile):
	# selectedFile = req.form['fisier']
	imgFolderListing = ''
	# os_usrname = os.getenv('USER')
	# if selectedFile.filename:
	if submittedFile.filename:
		# imgFolder = os.path.join('var', 'www', 'soc', 'res', 'img')
		imgFolder = os.path.join('/', 'var', 'www', 'uidpics')
		# path2newImg = os.path.join(imgFolder, selectedFile.filename)
		path2newImg = os.path.join(imgFolder, submittedFile.filename)
		# open(path2newImg, 'wb').write(selectedFile.file.read())
		open(path2newImg, 'wb').write(submittedFile.file.read())

		imgFolderListing = os.listdir(imgFolder)
	# return generateDir()
	"""
	s = """\
	"""
	<html>
		<body>
			<h1>Uploaded your image: %s </h1>
			<p>User[%s]in working dir: %s </p>
			<p>images folder listing (%s) : %s </p>
		</body>
	</html>
	"""
	"""
	return s % (selectedFile.filename, os_usrname, os.getcwd(), imgFolder, imgFolderListing)	
	"""

def form(req):
	name = req.form['losername']
	coo = Cookie.get_cookies(req)
	
	selectedFile = req.form['fisier']

	"""
	great tutorial http://lost-and-found-narihiro.blogspot.ro/2013/07/apache-modpython-upload-files-over-post.html
	"""
	s = """\
	<html>
		<body>
			<h1>Yo! %s &nbsp; &nbsp; &nbsp;%s and file: %s %s</h1>
			<p>in working dir: %s </p>
			<p>images folder listing: %s </p>
		</body>
	</html>
	"""
	path2img = os.path.join('var', 'www', 'soc', 'res', 'img')
	return s % (name, coo['manca'], req.method, os.path.join(path2img, selectedFile.filename), os.getcwd(), os.listdir(os.path.join(path2img)))

def index(req):
	charSet = 'abcdefghijlmnopqtsrvwxz1234567890ABCDEFGHIJLMNOPQTSRVWXZ'
	tstamp = time.time() + 2000
	a_cookie = Cookie.Cookie('mySweetAuth', mmfao2K98Lbkkg(charSet, 12) + '__' + str(tstamp))
	a_cookie.expires = tstamp
	Cookie.add_cookie(req, a_cookie)
	return generateDir(req, 'index')
	"""
		Generates the directory page content (profile boxes) - this is a actual page
		!! might be duplicate for def generateDir()
	"""
	# cookies = mod_python.Cookie.get_cookies(req)

	# cookies = Cookie.SimpleCookie()
	# print cookies['manca'].value
	

	"""
	conn = sqlite3.connect("/var/www/m/site.db")

	cur = conn.cursor()
	cur.execute("select * from newusers;")

	rows = cur.fetchall()

	directory = "";
	# directory = str(rows[0]) + "";

				# <img src=" "" + i[2] +"" style="max-width:160px; max-height:160px;" >
	for i in rows:
		# profBox = "<div><p>" +i[1]+ "</p></div>"
		profBox = ""\
		<div id="userprofilebox">
			<div id="profileImg">
				<img src="../"" + i[2] + "" style="max-width:160px; max-height:160px;" >
			</div>
			<div id="profileDescription">
				<hr width=90%>
				<p>Name:&nbsp;&nbsp;&nbsp;"" + i[1] + ""</p>
				<p>Occupation:&nbsp;&nbsp;"" + i[5] + ""</p>
			</div>
			<div id="profileLastInfo">
				<p>Last login:&nbsp;&nbsp;&nbsp;"" + i[4] +""</p>
			</div>
		</div>
		""
		directory += profBox

	s = ""\
	<html>
	<head>
		<link rel="stylesheet" type="text/css" href="../soc/res/css/main.css">
		<title>Set from Python	</title>
	</head>
		<body>
			<h1>Welcome message from Danny </h1>
			"" + directory + ""
			<!-- <img src="http://www.wild-scotland.org.uk/wp-content/uploads/2014/02/160x160Avatar-2.jpg">-->
		</body>
	</html>
	return s
	"""
