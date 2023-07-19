from pyzkaccess import ZKAccess, ZK200, ZK100, ZK400
from pyzkaccess.tables import User

connstr = "protocol=TCP,ipaddress=149.3.34.167,port=4370,timeout=10000,passwd="
with ZKAccess(connstr=connstr, device_model=ZK200) as zk:
    for record in zk.table('User'): 
        print(record)

def add_user(card, pin, password):
    try:
        with ZKAccess(connstr=connstr, device_model=ZK200) as zk:
            user = User(card=card, pin='123', password='555',
                        super_authorize=False).with_zk(zk)
            user.save()
    except Exception as ex:
        print(str(ex))
        return False
    return True


def delete_user(card):
    try:
        with ZKAccess(connstr=connstr, device_model=ZK200) as zk:
            user = User(card=card, pin='123', password='555',
                        super_authorize=False).with_zk(zk)
            user.save()
    except Exception as ex:
        print(str(ex))
        return False
    return True
