// Extension Script For About Page
function mail_color_changer() {
    if (theme_mode==="dark") {
        document.getElementById("contact_mail").style.color = "red"
    } else {
        document.getElementById("contact_mail").style.color = "blue"
    }
}
function mail_color_remover() {
    if (theme_mode==="dark") {
        document.getElementById("contact_mail").style.color = "white"
    } else {
        document.getElementById("contact_mail").style.color = "black"
    }
}
function t_c_e_extender(theme) {
    if (theme==="dark") {
        document.getElementById("about_username").style.borderColor = "white"
        document.getElementById("logo_desc").style.borderColor = "white"
        document.getElementById("logo_desc_1").style.borderColor = "white"
        document.getElementById("logo_desc_2").style.borderColor = "white"
        document.getElementById("logo_desc_3").style.borderColor = "white"
        document.getElementById("logo_desc_4").style.borderColor = "white"
        document.getElementById("separator3").innerHTML = '<hr width="auto" size="1" color"white">'
        document.getElementById("contact_mail").style.color = "white"
    } else {
        document.getElementById("about_username").style.borderColor = "black"
        document.getElementById("logo_desc").style.borderColor = "black"
        document.getElementById("logo_desc_1").style.borderColor = "black"
        document.getElementById("logo_desc_2").style.borderColor = "black"
        document.getElementById("logo_desc_3").style.borderColor = "black"
        document.getElementById("logo_desc_4").style.borderColor = "black"
        document.getElementById("separator3").innerHTML = '<hr width="auto" size="1" color"black">'
        document.getElementById("contact_mail").style.color = "black"
    }
}