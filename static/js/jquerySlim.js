function $q(query)
{
    if(!query || query.length <= 1)
    {
        return false;
    }

    var classQuery = query.startsWith(".");
    var idQuery = query.startsWith("#");


    var result = false;
    query = query.substr(1);
    console.log("Result1:", result)
    if(classQuery)
    {
        var temp_result = document.getElementsByClassName(query);
        if(temp_result && temp_result.length >= 1)
        {
            result = temp_result[0];
        }
    }
    else if(idQuery)
    {
        result = document.getElementById(query);
    }
    if(result)
    {
        return objectify(result);
    }
    return false;
};

function objectify(HTMLObject)
{
    var obj = {
        HTML:HTMLObject,
        attr: function(attributeName, value)
        {
            try
            {
                var result = false;
                if(attributeName)
                {
                    if(value)
                    {
                            this.HTML.setAttribute(attributeName, value);
                            result = true; 
                    }
                    else
                    {
                        result = this.HTML.getAttribute(attributeName);
                    }
                }
                return result
            }
            catch (error) {
                console.error(error);
                return result;
            }      
        },
        css: function(propertyName, value)
        {
            try
            {
                var result = false;
                if(propertyName)
                {
                    if(value)
                    {
                        this.HTML.style[propertyName] = value;
                        result = true;
                    }
                    else
                    {
                        result = this.HTML.style[propertyName];
                        if(result.length == 0)
                        {
                            var elem = this.HTML;
                            var elementStyle = elem.style;
                            var computedStyle = window.getComputedStyle(elem, null);

                            for (prop in elementStyle) {
                                if (elementStyle.hasOwnProperty(prop)) {
                                    if(prop === propertyName)
                                    {
                                        result = computedStyle[prop];
                                        break;
                                    }
                                }
                            }
                        }
                    }
                }  
            }
            catch(error)
            {
                console.error(error);
            }
            return result
        },

        html: function(htmlString)
        {
            try
            {
                var result = false;
                if(htmlString)
                {
                    this.HTML.innerHTML = htmlString;
                    result = true;
                }
                else
                {
                    result = this.HTML.innerHTML;
                }
            }
            catch(error)
            {
                console.error(error);
            }
            return result;
        },
        text: function(text)
        {
            try
            {
                var result = false;
                if(text)
                {
                    this.HTML.textContent = text;
                    result = true;
                }
                else
                {
                    result = this.HTML.textContent;
                }
            }
            catch(error)
            {
                console.error(error);
            }
            return result;
        },
        val: function(value)
        {
            try
            {
                var result = false;
                if(value)
                {
                    this.HTML.value = value;
                    result = true;
                }
                else
                {
                    result = this.HTML.value || false;
                }
            }
            catch(error)
            {
                console.error(error);
            }
            return result;
        }
    }

    return obj;
}