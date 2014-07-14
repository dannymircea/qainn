/* User registration form */
function inputColorFadeIn(currentElement) {
	// this function is for a visual efect
	var minColor = 0xB0B0B0;
	var myInterval = setInterval( // declared as a var in order to be able to call clearInterval()
		function() {
			if (minColor > 0xEFEFEF) {
				clearInterval(myInterval);
			} else {
				document.getElementById(currentElement.id).style.backgroundColor = "#" + minColor.toString(16).toUpperCase();
				document.getElementById(currentElement.id).style.color = "#000000";
				minColor += 0x080808;
			}
		}, 20) // closing setInterval
}

function inputColorFadeOut(currentElement) {
	// this function is for a visual efect
	var maxColor = 0xEFEFEF;
	var myInterval = setInterval( // declared as a var in order to be able to call clearInterval()
		function() {
			if (maxColor == 0xAFAFAF) {
				clearInterval(myInterval);
			} else {
				document.getElementById(currentElement.id).style.backgroundColor = "#" + maxColor.toString(16).toUpperCase();
				document.getElementById(currentElement.id).style.color = "#FFFFFF";
				maxColor -= 0x080808;
			}
		}, 20) // closing setInterval
}

function setErrInfBox(errmsgbox, displayStat, string2display) {
	// for displayStat choose between 'none' and 'block'
	errmsgbox.style.display = displayStat;
	errmsgbox.textContent = string2display;
}

function validate(field) {
	var currId = field.id;
	var currElement = document.getElementById(currId);
	var currElementErrInf = document.getElementById(currId + "errinf");
	// alert("got Fieldvalue:"+ currId);
	switch(currId) {
		case 'username_f':
			if (currElement.value.length < 6) {
				setErrInfBox(currElementErrInf, 'block', 'username is too short!')
			} else if (currElement.value.length > 10) {
				setErrInfBox(currElementErrInf, 'block', 'username is too long!')
			} else {
				setErrInfBox(currElementErrInf, 'none', '')
			}
			break;
		case 'fulluser_f':
			if (currElement.value.length > 20) {
				setErrInfBox(currElementErrInf, 'block', 'full username is too long!')
			} else {
				setErrInfBox(currElementErrInf, 'none', '')
			}
			break;
		case 'email_f':
			if (currElement.value.length > 20) {
				setErrInfBox(currElementErrInf, 'block', 'email is not OK')
			} else {
				setErrInfBox(currElementErrInf, 'none', '')
			}
			break;
		default:
			document.getElementById('username_flbl').innerHTML = "Username errordefault:"
	}
}
			
	
