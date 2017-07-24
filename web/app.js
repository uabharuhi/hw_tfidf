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
    xobj.open('GET',filename, false); //  sync request , false 
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
	var tfidf_obj = null;
	if(typeof Storage !== "undefined"){
		  // Yes! localStorage and sessionStorage support!
		  // Some code.....
		console.log('support');
		localStorage.removeItem("tfidf");
		console.log('after removeItem');
		console.log(localStorage.getItem("tfidf")); 

		load_tfidf('./tfidf.json'); //sync to work
		tfidf_obj = JSON.parse(localStorage.getItem("tfidf"));
		console.log('abcdefg');
		console.log(tfidf_obj);

		function click_callback(){
			console.log('click btn');
			var query_text = $('#query_input').val();
			console.log(tfidf_obj); //closure
			//retrieve data and sorted and append dom structure
			//retrieve data

			candidates={} //key is document number ,value is tfidf value
			for (var i=0 ; i< tfidf_obj.length ; ++i) {
				var tf_set = tfidf_obj[i];
				
				//console.log(tf_set);
				//console.log(i);
  				if(query_text in tf_set){
  					candidates[i] = tf_set[query_text]
  				}
  			}
  				// test grep ".\{1,10\}has.\{1,10\}" tfidf.json  -o | head -n 10
  				//sort
			keysorted = Object.keys(candidates); //closure
			//remove all previous result
			$( ".res" ).remove();
			console.log('1234')
			//console.log(candidates.length)
			var s = '';
			for(var j=0;j<keysorted.length;++j){
				//console.log(j);
				key = keysorted[j];
				s = s +`<tr class='res'><td>${key}</td><td>${candidates[key]}</td></tr>`;

			}
			$("#show tr:last").after(s);


			
			console.log(candidates);

		};


		$('#query_btn').on("click",click_callback);
		
	}
	else{
		  // Sorry! No web storage support..
		window.alert('GG your browser doesnt supprt localStorage.........');
	}

});
