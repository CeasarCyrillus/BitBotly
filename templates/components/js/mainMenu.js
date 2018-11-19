
function openMainMenu()
{   var btn = document.getElementById("menuIcon");
    var menu = document.getElementById("mainMenu");
    btn.setAttribute("status", "open");
    menu.classList.add("show");
    menu.setAttribute("status", "open");
    return;
}

function closeMainMenu()
{
    var btn = document.getElementById("menuIcon");
    var menu = document.getElementById("mainMenu");
    btn.setAttribute("status", "closed");
    menu.classList.remove("show");
    menu.setAttribute("status", "closed");
    return;
}

function toggleMainMenu()
{
    btn = document.getElementById("menuIcon");
    var status = btn.getAttribute("status");
    closeCurrentMenu();
    switch(status)
    {
        case "open":
            closeMainMenu();
            break;
        case "closed":
            openMainMenu();

            break;
        default:
            closeMainMenu();
    }
    return;
}