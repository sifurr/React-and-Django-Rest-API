// C => Create => POST
// R => Retrieve => GET
// U => Update => PUT/PATCH
// D => Delete => DELETE



// GET Request
// axios.get("http://127.0.0.1:8000/apiV1/status/list")
// .then(response => console.log(response))


// get DETAIL
// axios.get("http://127.0.0.1:8000/apiV1/status/detail/2")
// .then(response => console.log(response))



// POST Request
// let status = {
// 	user: 4,
// 	content: "I am test data!",
// 	image:  null
// }

// axios.post("http://127.0.0.1:8000/apiV1/status/create/", status, {
// 	headers:{
// 		 "Content-Type": "application/json"
// 	}
// })
// .then(response => console.log(response))
// .catch(error => console.log(error))


// DELETE
// axios.delete("http://127.0.0.1:8000/apiV1/status/delete/5/")
// .then(response => console.log(response))
// .catch(error => console.log(error))


// PUT request uses all properties 
// let updatedStatus = {
// 	user: 2,
// 	content: "I have been updated using PUT request",
// 	image:  null
// }

// axios.put("http://127.0.0.1:8000/apiV1/status/update/4/", updatedStatus, {
// 	headers:{
// 		 "Content-Type": "application/json"
// 	}
// })
// .then(response => console.log(response))
// .catch(error => console.log(error))

// PATCH is hassle free then PUT

// PATCH request uses only particular property
let updatedStatus = {
	content: "I have been updated using PATCH request",
}

axios.patch("http://127.0.0.1:8000/apiV1/status/update/4/", updatedStatus, {
	headers:{
		 "Content-Type": "application/json"
	}
})
.then(response => console.log(response))
.catch(error => console.log(error))