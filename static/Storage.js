// done
function SaveItem(numOfWeek) {
			
	var name = document.getElementById("name"+numOfWeek).value;
	var data = document.getElementById("data"+numOfWeek).value;
	var goals = localStorage[numOfWeek] ? JSON.parse(localStorage[numOfWeek]) : {} ;
	goals[name] = data;

	localStorage.setItem(numOfWeek, JSON.stringify(goals));
	doShowAll(numOfWeek);
	
}

function ModifyItem(numOfWeek) {
	var name = document.forms.goalsList.name.value;
	document.forms.goalsList.data.value = localStorage.getItem(name);
	doShowAll();
}

function RemoveItem(numOfWeek) {
	var name = document.forms.goalsList.name.value;
	document.forms.goalsList.data.value = localStorage.removeItem(name);
	doShowAll();
}
// done
function ClearAll(numOfWeek) {
	delete localStorage[numOfWeek];
	doShowAll(numOfWeek);
}

//done
function doShowAll(numOfWeek) {
	if (CheckBrowser()) {
		var key = "";
		var list = "<tr><th>Goal</th><th>Recurrence</th></tr>\n";
		var i = 0;
		var goals = localStorage[numOfWeek] ? JSON.parse(localStorage[numOfWeek]) : {};
		var goalsKeys = Object.keys(goals);
		for (i = 0; i <= goalsKeys.length - 1; i++) {
			key = goalsKeys[i];
			list += "<tr contenteditable><td>" + key + "</td>\n<td>"
					+ goals[key] + "</td></tr>\n";
		}
		if (list == "<tr><th>Goal</th><th>Recurrence</th></tr>\n") {
			list += "<tr><td><i>nothin' here</i></td>\n<td><i>nothin' here either</i></td></tr>\n";
		}
		document.getElementById('list'+numOfWeek).innerHTML = list;
	} else {
		alert('Cannot store shopping list as your browser do not support local storage');
	}
}

function CheckBrowser() {
	if ('localStorage' in window && window['localStorage'] !== null) {

		return true;
	} else {
			return false;
	}
}

