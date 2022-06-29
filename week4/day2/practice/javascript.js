const container1 = document.getElementById("container");
const textbox1 = document.getElementById("textbox");
// const textbox2 = document.get
const submitButton1 = document.getElementById("submitButton");
const input1 = document.getElementById("input");

function saveInput(){
    let newitem = document.createElement("li")
    newitem.textContent = input1.value
    container1.append(newitem)
}

submitButton1.onclick = () => saveInput()


