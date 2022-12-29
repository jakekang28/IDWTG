
const writeButton = document.querySelector("#write")


writeButton.addEventListener("click", write)

function write(){
    return window.location.assign("http://localhost:3002/write")
}


