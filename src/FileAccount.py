import json


def _account_details(id, pwd):
    return json.loads('{"id": "' + id + '", "password": "' + pwd + '"}')


class FileAccount:
    def __init__(self, cipher, filename):
        self.filename = filename
        self.cipher = cipher

        with open(self.filename, 'rb') as f:
            data = f.read()

        self.content = json.loads(self.cipher.decrypt(data))

    def get_content(self):
        return self.content

    def add_entry(self, title, id, pwd, details):
        self.content["accounts"][title] = _account_details(id, pwd)
        if details:
            self.content["accounts"][title]["extra_details"] = details

        with open(self.filename, 'wb') as f:
            f.write(self.cipher.encrypt(json.dumps(self.content)))

    def remove_entry(self, title):
        try:
            del self.content["accounts"][title]
            with open(self.filename, 'wb') as f:
                f.write(self.cipher.encrypt(json.dumps(self.content)))
        except KeyError:
            print("this entry does not exist")

    def list_all_accounts(self):
        for account in self.content["accounts"]:
            print(account)
            print("----------")
            print("Identifier: " + str(self.content["accounts"][account]["id"]))
            print("Password: " + str(self.content["accounts"][account]["password"]))
            ## Add recursive function to read extra info
            print("\n")
