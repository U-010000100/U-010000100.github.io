// Main Script For All Pages
var theme_mode = "light"
function hover_color_changer_1(){
    if (theme_mode==="dark") {
        document.getElementById("link1").style.color = "red"
    } else {
        document.getElementById("link1").style.color = "blue"
    }
}
function hover_color_changer_2(){
    if (theme_mode==="dark") {
        document.getElementById("link2").style.color = "red"
    } else {
        document.getElementById("link2").style.color = "blue"
    }
}
function hover_color_changer_3(){
    if (theme_mode==="dark") {
        document.getElementById("link3").style.color = "red"
    } else {
        document.getElementById("link3").style.color = "blue"
    }
}
function hover_color_changer_4(){
    if (theme_mode==="dark") {
        document.getElementById("link4").style.color = "red"
    } else {
        document.getElementById("link4").style.color = "blue"
    }
}
function hover_color_changer_5(){
    if (theme_mode==="dark") {
        document.getElementById("link5").style.color = "red"
    } else {
        document.getElementById("link5").style.color = "blue"
    }
}
function hover_color_remover_1(){
    if (theme_mode==="dark") {
        document.getElementById("link1").style.color = "white"
    } else {
        document.getElementById("link1").style.color = "black"
    }
}
function hover_color_remover_2(){
    if (theme_mode==="dark") {
        document.getElementById("link2").style.color = "white"
    } else {
        document.getElementById("link2").style.color = "black"
    }
}
function hover_color_remover_3(){
    if (theme_mode==="dark") {
        document.getElementById("link3").style.color = "white"
    } else {
        document.getElementById("link3").style.color = "black"
    }
}
function hover_color_remover_4(){
    if (theme_mode==="dark") {
        document.getElementById("link4").style.color = "white"
    } else {
        document.getElementById("link4").style.color = "black"
    }
}
function hover_color_remover_5(){
    if (theme_mode==="dark") {
        document.getElementById("link5").style.color = "white"
    } else {
        document.getElementById("link5").style.color = "black"
    }
}
function theme_color_changer() {
    const element = document.getElementById("themechanger").style
    if (theme_mode==="dark") {
        element.color = "black"; element.backgroundColor = "white"
        document.getElementById("themechanger").innerText = "Light Theme"
    } else {
        element.color = "white"; element.backgroundColor = "black"
        document.getElementById("themechanger").innerText = "Dark Theme"
    }
}
function theme_color_remover() {
    const element = document.getElementById("themechanger").style
    if (theme_mode==="dark") {
        element.color = "white"; element.backgroundColor = "black"
        document.getElementById("themechanger").innerText = "Dark Theme"
    } else {
        element.color = "black"; element.backgroundColor = "white"
        document.getElementById("themechanger").innerText = "Light Theme"
    }
}
function theme_changer() {
    if (theme_mode==="light") {
        theme_mode = "dark"
        document.getElementById("themechanger").style.borderColor = "white"
        document.getElementById("themechanger").style.color = "black"
        document.getElementById("themechanger").style.backgroundColor = "white"
        document.getElementById("themechanger").innerText = "Light Theme"
        document.getElementById("dp_header").style.borderColor = "white"
        document.getElementById("link1").style.color = "white"
        document.getElementById("link2").style.color = "white"
        document.getElementById("link3").style.color = "white"
        document.getElementById("link4").style.color = "white"
        document.getElementById("link5").style.color = "white"
        document.getElementById("header").style.backgroundColor = "black"
        document.getElementById("footer").style.color = "white"
        document.getElementById("footer").style.backgroundColor = "black"
        document.getElementById("separator1").innerHTML = '<hr width="auto" size="2" color="white">'
        document.getElementById("separator2").innerHTML = '<hr width="auto" size="2" color="white">'
    } else {
        theme_mode = "light"
        document.getElementById("themechanger").style.borderColor = "black"
        document.getElementById("themechanger").style.color = "white"
        document.getElementById("themechanger").style.backgroundColor = "black"
        document.getElementById("themechanger").innerText = "Dark Theme"
        document.getElementById("dp_header").style.borderColor = "black"
        document.getElementById("link1").style.color = "black"
        document.getElementById("link2").style.color = "black"
        document.getElementById("link3").style.color = "black"
        document.getElementById("link4").style.color = "black"
        document.getElementById("link5").style.color = "black"
        document.getElementById("header").style.backgroundColor = "white"
        document.getElementById("footer").style.color = "black"
        document.getElementById("footer").style.backgroundColor = "white"
        document.getElementById("separator1").innerHTML = '<hr width="auto" size="2" color="black">'
        document.getElementById("separator2").innerHTML = '<hr width="auto" size="2" color="black">'
    }
    theme_changer_extension(theme_mode)
}