

const cursor = document.getElementById("cursor-custom"),
  radius = cursor.offsetHeight / 2;

document.addEventListener("mousemove", (e) => {
  let top = e.clientY - radius,
    left = e.clientX - radius;
  console.log("bip")
  cursor.style = `top: ${top}px; left: ${left}px`;
});