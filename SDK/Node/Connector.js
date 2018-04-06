var request = require('request');
var fs = require('fs');


var data = fs.readFileSync('config.json', 'utf8');
var conf = JSON.parse(data);

var baseurl = conf[0].baseurl;
var port = conf[0].port;
//var pass = conf[0].pass;

// function validate(param) {
// 	var temp;
	
// 	request(baseurl+":"+port+"/"+param, function (error, response, body) {
// 		//console.log('error:', error); // Print the error if one occurred
// 		//console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
// 		//console.log('body:', body); // Print the HTML for the Google homepage.
		
// 		temp = body;
// 	});

// return temp;
// }

function val(param) {
	var myJSONObject = { par:'value' };
	request({
	    url: "http://localhost:5000/val",
	    method: "POST",
	    json: true,   // <--Very important!!!
	    body: myJSONObject
	}, function (error, response, body){
		console.log(error);
    	console.log(response);
    	return body;
	});
}

console.log(val('vipul'));
