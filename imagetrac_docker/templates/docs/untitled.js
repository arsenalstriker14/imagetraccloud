function addem(arr){
	count = 0;
	for (var i = 0; i < arr.length; i++){
		count += arr[i]
	}
	return count
}

function randomNumber(upper){
	return Math.floor(Math.random() * upper) + 1;
}

var counter = 0
while (counter < 6){
	var randNum = randomNumber(6);
	console.log(randNum + ' ');
	counter += 1
}


function guessIt(){
	var counter = 0;
	var guess = 0;
	var randNum = Math.floor(Math.random() * 10000) + 1;
	while (guess != randNum){
		guess = Math.floor(Math.random() * 10000) + 1;
		counter += 1;
	}
	return guess + " " + counter;

}



var request = {};
request = new XMLHttpRequest();
request.open('GET', 'http://localhost/docs/data.json')
request.onreadystatechange = function(){
	if((request.readyState == 4) && (request.status == 200)){
		console.log(responseText)
	}
}
request.send()