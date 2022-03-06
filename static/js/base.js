console.log("This is a message");

let mainCB = document.getElementById("task-check");
let mainLabel = document.getElementById("task-label");
let trashIcon = document.querySelector("svg");

mainCB.addEventListener('click', () => {
    mainLabel.classList.toggle('line-through')
});