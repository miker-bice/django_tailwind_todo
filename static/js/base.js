console.log("This is a message");

const mainCB = document.querySelector("input.task-check");
// let mainLabel = document.getElementById("task-label");
// let trashIcon = document.querySelector("svg");
//
// mainCB.addEventListener('click', () => {
//     mainLabel.classList.toggle('line-through')
// });

const listContainer = document.getElementById("list-item-container");

mainCB.addEventListener("click", () => {
    listContainer.classList.toggle("bg-slate-600")
});
