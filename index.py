# name, #email, #ctype, #msg

# add_com() -> cid, + status
import datetime
import json
from textwrap import indent


class CMS:
    def __init__(self, name, email, phone, ctype, msg):
        self.name = name
        self.email = email
        self.ctype = ctype
        self.msg = msg
        self.phone = phone
        self.dateTime = datetime.datetime.now()


class ADD_CMS(CMS):
    def __init__(self, name, email, phone, ctype, msg, cid, status):
        super().__init__(name, email, phone, ctype, msg)
        self.cid = cid
        self.status = status

    def addData(self):
        dataAdd = {
            "id": self.cid,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "cype": self.ctype,
            "complaint": self.msg,
            "status": self.status
        }
        with open('datas.json', "r") as file:
            data = json.load(file)

        # Modify the data
        data['complainants'].append(dataAdd)
        # Update the "last-update" field
        data['id'][0]['last-update'] = str(self.dateTime)
        # Update the "last-update" field
        data['id'][0]['track-id'] = self.cid

        # Write the modified data back to the file
        with open('datas.json', "w") as file:
            json.dump(data, file, indent=4)
        print('------ Data Added ------')
  



with open('datas.json', 'r+') as file:
    data = json.load(file)

userIn = ''
while userIn != 'q':
    print(f'ADD (1) | Manage(2) | Quit(q)')
    getIn = input()
    if getIn == '1':
        name = input('name: ')
        email = input('email: ')
        phone = input('phone: ')
        ctype = input('Ctype: ')
        msg = input('msg: ')

        add_cms = ADD_CMS(name, email, phone, ctype, msg,
                          (data['id'][0]['track-id']+1), 'opened')
        add_cms.addData()
    elif getIn == '2':
        with open('datas.json', 'r') as file:
            dataM = json.load(file)
            print(dataM['complainants'])
    elif getIn == 'q':
        userIn = 'q'
