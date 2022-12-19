function change() {
    var prompt = document.getElementById("Ask")

    var entry = {
    prompt: prompt.value
}

fetch(`${window.origin}/getAnswer`, {
method: "POST",
credentials:"include",
body:JSON.stringify(entry),
cache:"no-cache",
headers: new Headers({
    "content-type": "application/json"
})
})
.then(function(response){
if (response.status !== 200){
    alert('Something Went Wrong')
    return ;
}

response.json().then(function(data){
    var textareaText = document.getElementById("text_area").value = ""; 
    var newText = data.answer; 
    document.getElementById("text_area").value = newText;
})

})

}