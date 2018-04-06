<?php 

$str = file_get_contents('config.json');
$conf = json_decode($str, true); // decode the JSON into an associative array

global $baseurl = $conf[0]['baseurl'];
global $port = $conf[0]['port'];

function validate($param) {
	// //global $baseurl;
	// $ch = curl_init($baseurl.':'.$port.'/val'); // such as http://example.com/example.xml

	// curl_setopt($ch, CURLOPT_POST, 1);
	// curl_setopt($ch, CURLOPT_POSTFIELDS,
 //            'par='.$param);
	// curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	// curl_setopt($ch, CURLOPT_HEADER, 0);

	// $data = curl_exec($ch);
	// curl_close($ch);
	
	// return $data;

	// set post fields
	$post = [
	    'par' => $param,
	];

	$ch = curl_init($baseurl.':'.$port.'/val');
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_POSTFIELDS, $post);

	// execute!
	$response = curl_exec($ch);

	// close the connection, release resources used
	curl_close($ch);

	// do anything you want with your response
	return $response; // return the response
	
	//echo $data;
}

function val($param) {
	
	$r = new HttpRequest('http://localhost:5000/'.$param, HttpRequest::METH_GET);
	$r->setOptions(array('lastmodified' => filemtime('local.rss')));
	$r->addQueryData(array('category' => 3));
	try {
		$r->send();
		if ($r->getResponseCode() == 200) {
			file_put_contents('local.rss', $r->getResponseBody());
		}
	} catch (HttpException $ex) {
		echo $ex;
	}
}
?>