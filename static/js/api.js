function send_to_api(url, success_cb, fail_cb, data, content_type='application/json; charset=UTF-8')
{
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader('Content-Type', content_type);
    xhr.onload = function (e)
    {
        if (xhr.readyState === 4)
        {
            if (xhr.status === 200)
            {
                if(content_type == 'application/json; charset=UTF-8')
                {
                    success_cb(JSON.parse(xhr.responseText));
                }
                else
                {
                    success_cb(xhr.responseText);
                }
                
            }
            else
            {
                fail_cb(xhr.statusText);
            }
        }
    };

    xhr.onerror = function (e) {
    console.error(xhr.statusText);
    };

    xhr.send(JSON.stringify(data));
}