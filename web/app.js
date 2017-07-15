/**
 * 
 * @authors Your Name (you@example.org)
 * @date    2017-07-15 14:39:27
 * @version $Id$
 */

// code from https://codepen.io/KryptoniteDove/post/load-json-file-locally-using-pure-javascript

function loadJSON(filename , callback) {   
    var xobj = new XMLHttpRequest();
        xobj.overrideMimeType("application/json");
    xobj.open('GET',filename, true); // Replace 'my_data' with the path to your file
    xobj.onreadystatechange = function () {
          if (xobj.readyState == 4 && xobj.status == "200") {
            // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
             callback(xobj.responseText);
          }
    };
    xobj.send(null);  
 }


function load_tfidf(filename){
	var actual_JSON = null;
	actual_JSON = loadJSON(filename , function(response) {
  		// Parse JSON string into object
   		var res = JSON.parse(response);
   		console.log('get tfidf');
   		console.log(res);
   		localStorage.setItem("tfidf",response);

 	});
 	console.log('json .............');
	console.log(actual_JSON);
 	return actual_JSON;

}


$(document).ready(function(){
	//load tf idf data from json

	if(typeof Storage !== "undefined"){
		  // Yes! localStorage and sessionStorage support!
		  // Some code.....
		console.log('support');
		localStorage.removeItem("tfidf");
		load_tfidf('./tfidf.json');
	}
	else{
		  // Sorry! No web storage support..
		window.alert('GG your browser doesnt supprt localStorage.........');

	}

	$('#query_btn').on("click",function(){
		console.log('click btn');
		var query_text = $('#query_input').val();
		console.log('q text');
		console.log(query_text);
		tfidf_obj = JSON.parse(localStorage.getItem("tfidf"));

		console.log(tfidf_obj);
	});


});
//localStorage.setItem("lastname");
//localStorage.getItem("lastname");
//localStorage.removeItem("lastname");