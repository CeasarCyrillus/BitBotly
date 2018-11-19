function openMainMenu()
{var btn=document.getElementById("menuIcon");var menu=document.getElementById("mainMenu");btn.setAttribute("status","open");menu.classList.add("show");menu.setAttribute("status","open");return;}
function closeMainMenu()
{var btn=document.getElementById("menuIcon");var menu=document.getElementById("mainMenu");btn.setAttribute("status","closed");menu.classList.remove("show");menu.setAttribute("status","closed");return;}
function toggleMainMenu()
{btn=document.getElementById("menuIcon");var status=btn.getAttribute("status");closeCurrentMenu();switch(status)
{case"open":closeMainMenu();break;case"closed":openMainMenu();break;default:closeMainMenu();}
return;}
function openMenu(menu)
{menu.setAttribute("status","open");return;}
function closeMenu(menu)
{menu.setAttribute("status","closed");return;}
function toggleMenu(menuId)
{toggleMainMenu();var menu=document.getElementById(menuId);var status=menu.getAttribute("status");switch(status)
{case"open":closeMenu(menu);break;case"closed":openMenu(menu);break;default:closeMenu(menu);}
return;}
function closeCurrentMenu()
{var btnId=event.target.getAttribute("id");if(btnId!="menuIcon")
{var menuId=event.target.parentNode.getAttribute("id");var menu=document.getElementById(menuId);closeMenu(menu);}
else
{var open_menues=$(".menuBase[status='open']")
for(var i=0;i<open_menues.length;i++)
{var menu=open_menues[i];var menu_id=menu.getAttribute("id");if(menu_id!="mainMenu")
{closeMenu(menu);}}}
return;}
function deletePersonalData(model_attr)
{var printable_name=this.event.target.getAttribute("data-label")||false;var btn=this.event.target||false;var input=this.event.target.parentNode.children[1];console.log(input);if(printable_name&&btn)
{vex.dialog.confirm({message:"Delete "+printable_name+" from your account permanently?",callback:function(yes){if(yes){send_to_api("/api/deletePersonalData",function()
{input.setAttribute("value","");vex.dialog.alert({message:"Succesfully deleted "+printable_name})
$(btn).toggleClass("deleted");btn.removeAttribute("onclick");},function()
{vex.dialog.alert({message:"Could not delete "+printable_name+". Try again later"})},{"model_attr":model_attr})}}})}
else if(printable_name)
{vex.dialog.alert({message:"Could not delete "+printable_name+". Try again later"})}
else
{vex.dialog.alert({message:"Could not delete data. Try again later"})}}