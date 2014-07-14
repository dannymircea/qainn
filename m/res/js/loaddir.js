function loaddir() {
	// js array with src urls for images of profileboxes
	var avatars = [ "http://buyingvalue.com/wp-content/uploads/2011/03/tony_the_tiger-lg-200x200.jpg",
	"http://avatar-user.s.aeriastatic.com/96688505/33bfb8b6-18af-4621-ba79-ce9fbb4a6d00",
	"http://nrns-games.com/forums/download/file.php?avatar=27593_1387767317.png",
	"http://www.roleplaygateway.com/download/file.php?avatar=67368_1379829850.png",
	"http://www.compliancebuilding.com/wp-content/uploads/2010/10/dilbert-Disaster-Recovery-300x265.jpg",
	"http://avatarmaker.net/free-avatars/avatars/cartoons_229/the_simpsons_254/homer_beer_hat_avatar_100x100_66405.gif"
	];
	var avatarOcc = [ "Student",
	"Student",
	"PhD",
	"Technician",
	"Sous-chef",
	"Sys admin"
	];
	var avatarName = [ "Johnny",
	"Leroy",
	"Anca",
	"Shawn",
	"Deborah",
	"Ian"
	];
	var currentDirProfileBoxes = "";
	for (x=0; x < avatars.length; x++) {
		var generatedDirPBoxes = "<div id=\'userprofilebox\'><div id=\"profileImg\"> <img src=\"" + avatars[x] +"\"> </div> <div id=\"profileDescription\"> <hr width=90%><p>" + avatarName[x] + "</p><p>" + avatarOcc[x] + "</p></div><div id=\"profileLastInfo\"><Member since(a date)</p><p>Last login</p></div></div>";
		currentDirProfileBoxes += generatedDirPBoxes;
	}
	document.getElementById('mainDivMenuBtnContent').innerHTML = currentDirProfileBoxes;
}

function mouseoutMenuButton(buttonObject) {
	buttonObject.className = 'unselectedMenubtn';
}

function hoverMenuButton(buttonObject) {
	buttonObject.className = 'selectedMenubtn';
	button = buttonObject.textContent.trim().toLowerCase();
	// alert("Hovered : "+button + "-"+ buttonObject);
	if (button == 'socialize') {
		loaddir();
	} else if (button == 'how it works') {
		document.getElementById('mainDivMenuBtnContent').innerHTML = "<h1> How it really Works!</h1>";
	} 
}
