
function openMenu(menu)
{
    menu.setAttribute("status", "open");
    return;
}

function closeMenu(menu)
{
    menu.setAttribute("status", "closed");
    return;
}

function toggleMenu(menuId)
{
    toggleMainMenu();
    var menu = document.getElementById(menuId);
    var status = menu.getAttribute("status");
    
    switch(status)
    {
        case "open":
            closeMenu(menu);
            break;
        case "closed":
            openMenu(menu);
            break;
        default:
            closeMenu(menu);
    }
    return;
}

function closeCurrentMenu()
{
    var btnId = event.target.getAttribute("id");
    if(btnId != "menuIcon")
    {
        var menuId = event.target.parentNode.getAttribute("id");
        var menu = document.getElementById(menuId);
        closeMenu(menu);
    }
    else
    {
        var open_menues = $(".menuBase[status='open']")
        for(var i = 0; i < open_menues.length; i++)
        {
            var menu = open_menues[i];
            var menu_id = menu.getAttribute("id");
            if(menu_id != "mainMenu")
            {
                closeMenu(menu);
            }
        }
    }
    return;
}