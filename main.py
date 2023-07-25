from pyzkaccess import ZKAccess, ZK200, ZK100, ZK400
from pyzkaccess.tables import User
from datetime import datetime

connstr = "protocol=TCP,ipaddress=149.3.34.167,port=4370,timeout=10000,passwd="


def add_user(card, pin, ip):
    connstr = f"protocol=TCP,ipaddress={ip},port=4370,timeout=4000,passwd="
    try:
        with ZKAccess(connstr=connstr, device_model=ZK200) as zk:
            user = User(card=card, pin=pin, start_time=datetime.now(),
                        super_authorize=True).with_zk(zk)
            user.save()
            zk.aux_inputs.events.refresh()
            print(f"IP: {ip} CARD: {card} ADDED SUCCESS")
    except Exception as ex:
        print('TRY #2')
        try:
            with ZKAccess(connstr=connstr, device_model=ZK200) as zk:
                user = User(card=card, pin=pin, start_time=datetime.now(),
                            super_authorize=True).with_zk(zk)
                user.save()
                zk.aux_inputs.events.refresh()
                print(f"IP: {ip} CARD: {card} ADDED SUCCESS ON TRY #2")
        except Exception as ex:
            print(str(ex))
            return False
    return True


def delete_user(card, pin, ip):
    connstr = f"protocol=TCP,ipaddress={ip},port=4370,timeout=4000,passwd="
    try:
        with ZKAccess(connstr=connstr, device_model=ZK200) as zk:
            user = User(card=card, pin=pin,
                        super_authorize=True).with_zk(zk)
            user.delete()
            zk.aux_inputs.events.refresh()
            print(f"IP: {ip} CARD: {card} REMOVED SUCCESS")
    except Exception as ex:
        print('TRY #2')
        try:
            with ZKAccess(connstr=connstr, device_model=ZK200) as zk:
                user = User(card=card, pin=pin,
                            super_authorize=True).with_zk(zk)
                user.delete()
                zk.aux_inputs.events.refresh()
                print(f"IP: {ip} CARD: {card} REMOVED SUCCESS ON TRY #2")
        except Exception as ex:
            print(str(ex))
            return False
    return True


def get_users(ip):
    connstr = f"protocol=TCP,ipaddress={ip},port=4370,timeout=4000,passwd="
    res = {}
    try:
        with ZKAccess(connstr=connstr, device_model=ZK200) as zk:
            for record in zk.table('User'):
                res[record.pin] = {
                                    "card": record.card,
                                    "pin": record.pin,
                                   }
    except Exception as ex:
        print(str(ex))
        return {}
    return res
