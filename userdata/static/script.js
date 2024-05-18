// Responsive Navigation
let resonsive_menu = document.getElementById("responsive_menu");

resonsive_menu.style.display = "none"

let menu_button = document.getElementById("menu_bar")
menu_button.addEventListener('click', menu)
menu_button.src = "menu.png"

function menu() {
  if (resonsive_menu.style.display == "none") {
    resonsive_menu.style.display = "block"
    menu_button.src = "close.png"
  }
  else {
    resonsive_menu.style.display = "none"
    menu_button.src = "menu.png"
  }
}

//For Information Banner
var information_banner = document.getElementById("information-banner")
information_banner.style.display = "none"
var id_container = document.querySelectorAll(".id_container");
var password_container = document.querySelectorAll(".password_container");

var copy_id = document.querySelectorAll(".copy_id");

var copy_password = document.querySelectorAll(".copy_password");
let i = 0
// id_container.forEach(box => {
//     box.addEventListener('click', () => push_id());
//   });

//   password_container.forEach(box => {
//     box.addEventListener('click', () => push_passowrd());
//   });

for (i = 0; i < id_container.length; i++) {
  id_container[i].addEventListener('click', push_id)
  var copy = copy_id[i].innerHTML
  function push_id() {
    console.log(copy_id[0].innerHTML)
    navigator.clipboard.writeText(copy);
    information_banner.innerHTML = "Id Copy Successful";
    information_banner.style.display = "flex"
    setTimeout(hide_message, 3000);
    console.log(copy_id[i])
  }
}

for (i = 0; i < password_container.length; i++) {
  password_container[i].addEventListener("click", push_passowrd)
  var copyp = copy_password[i].innerHTML

  function push_passowrd(copy) {
    navigator.clipboard.writeText(copyp);
    console.log("Push Password")
    setTimeout(hide_message, 3000);
    information_banner.style.display = "flex"

    information_banner.innerHTML = "Password Copy Successful";
  }
}




function hide_message() {
  information_banner.style.display = "none"
  console.log("Hide ")
}

