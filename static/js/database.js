<<<<<<< HEAD
=======
const cursor = document.getElementById("cursor-custom"),
  radius = cursor.offsetHeight / 2;

document.addEventListener("mousemove", (e) => {
  let top = e.clientY - radius,
    left = e.clientX - radius;
  cursor.style = `top: ${top}px; left: ${left}px`;
});
>>>>>>> be71133 (add background hacker)
// import { MDCDataTable } from "@material/data-table";
// const dataTable = new MDCDataTable(document.querySelector(".mdc-data-table"));
