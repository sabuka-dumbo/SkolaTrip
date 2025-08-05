const span1 = document.getElementById("span1")
const span2 = document.getElementById("span2")
const span3 = document.getElementById("span3")
const menu = document.getElementById("menu");
const burgermenu = document.getElementById("burgermenu");
let open = false;
let cooldown = false;

burgermenu.addEventListener("click", () => {
  if (cooldown) return; 
  cooldown = true;

  if (!open) {
    span1.style.animation = "span1-open 0.4s forwards";
    span2.style.animation = "span2-open 0.4s forwards";
    span3.style.animation = "span3-open 0.4s forwards";
    menu.style.animation = "menu-open 0.4s forwards";
    open = true;
  } else {
    span1.style.animation = "span1-close 0.4s forwards";
    span2.style.animation = "span2-close 0.4s forwards";
    span3.style.animation = "span3-close 0.4s forwards";
    menu.style.animation = "menu-close 0.4s forwards";
    open = false;
  }

  setTimeout(() => cooldown = false, 400);
});