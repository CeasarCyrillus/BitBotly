function deletePersonalData(model_attr)
{
    var printable_name = this.event.target.getAttribute("data-label") || false;
    var btn = this.event.target || false;
    var input = this.event.target.parentNode.children[1];
    console.log(input);
    if(printable_name && btn)
    {
        vex.dialog.confirm({
            message: "Delete " + printable_name + " from your account permanently?",
            callback: function (yes) {
                if (yes) {

                    send_to_api("/api/deletePersonalData",
                    function()
                    {
                        input.setAttribute("value", "");
                        vex.dialog.alert({
                            message: "Succesfully deleted " + printable_name
                        })

                        $(btn).toggleClass("deleted");
                        btn.removeAttribute("onclick");
                    },
                    
                    function()
                    {
                        vex.dialog.alert({
                            message: "Could not delete " + printable_name + ". Try again later"
                        })
                    },
                    {"model_attr":model_attr})

                    
                }
            }
        })
    }
    else if(printable_name)
    {
        vex.dialog.alert({
            message: "Could not delete " + printable_name + ". Try again later"
        })
    }
    else
    {
        vex.dialog.alert({
            message: "Could not delete data. Try again later"
        })
    }
}