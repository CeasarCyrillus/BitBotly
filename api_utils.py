import json
class Response():
    def __init__(self):
        self.success = False
        self.msg = "ERROR"
        self.data = {}
        

    def send(self, success=False):
        if success:
            self.success = True
            if self.msg == "ERROR":
                self.msg = "OK"

        self.content = {"success":self.success, "data":self.data, "msg":self.msg}
        return json.dumps(self.content)