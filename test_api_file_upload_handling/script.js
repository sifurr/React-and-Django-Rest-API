document.getElementById('myform').addEventListener('submit', handleSubmit);
document.getElementById('image').addEventListener('change', handleImage);

let myImage = null

function handleImage(e) {
	myImage = e.target.files[0];
	// console.log(myImage);
}

function handleSubmit(e){
	e.preventDefault();
	let user = document.getElementById('user').value;
	let content = document.getElementById('content').value;

	let form_data = new FormData();
	form_data.append('user', user);
	form_data.append('content', content);
	form_data.append('image', myImage);

	// for (var [key, value] of form_data.entries()){
	// 	console.log(key, ": ", value);
	// }

	// POST request (create)
	// axios.post("http://127.0.0.1:8000/apiV1/status/", form_data, {
	// 	header:{
	// 		"Content-Type": "multipart/form-data"
	// 	}
	// })
	// .then(response => console.log(response))


	// 
		axios.put("http://127.0.0.1:8000/apiV1/status/6/", form_data, {
		header:{
			"Content-Type": "multipart/form-data"
		}
	})
	.then(response => console.log(response))
	
}