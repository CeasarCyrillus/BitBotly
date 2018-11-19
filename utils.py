from threading import Thread


def send_mail(header, content, to_email, from_email):
    data = {
        "personalizations": [
            {
            "to": [
                {
                "email": to_email
                }
            ],
            "subject": header
            }
        ],
        "from": {
            "email": from_email
        },
        "content": [
            {
            "type": "text/html",
            "value": content
            }
        ]
    }
    
    try:
        response = sg.client.mail.send.post(request_body=data)
        error = None
    except Exception as ex:
        error = str(ex)
    finally:
        mail = Mail(header, content, response.status_code, error, to_email, from_email)
        db.session.add(mail)
        db.session.commit()

def send_mail_async(header, content, to_email, from_email):
    Thread(target=send_mail, args=(header, content, to_email, from_email)).start()

from models import Mail
from init_app import db, sg