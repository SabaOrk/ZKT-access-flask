from pyzkaccess import ZKAccess, ZK200, ZK100, ZK400
from pyzkaccess.tables import User,UserAuthorize
from datetime import datetime

connstr = "protocol=TCP,ipaddress=149.3.34.167,port=4370,timeout=10000,passwd="



def add_user(card, pin, ip):
    connstr = f"protocol=TCP,ipaddress={ip},port=4370,timeout=4000,passwd="
    try:
        autorized = False
        with ZKAccess(connstr=connstr, device_model=ZK200) as zk:
            user = User(card=card, pin=pin, start_time=datetime.now(), end_time=datetime(9999, 12, 31, 23, 59, 59),
                        super_authorize=False).with_zk(zk)
            user.save()
            # zk.aux_inputs.events.refresh()
            # zk.aux_inputs[0:3].events.poll()
            with open('output.txt', 'a') as output:
        output.writeline(f"IP: {ip} CARD: {card} ADDED SUCCESS")
        
            for UserAuthorizeRecord in zk.table('UserAuthorize'):
                if UserAuthorizeRecord.pin == pin:
                    autorized = True
                    with open('output.txt', 'a') as output:
        output.writeline('almost authorized')
            if  autorized == False:
                userAuthorize = UserAuthorize(pin=pin,timezone_id=1,doors=(True, True, True, True)).with_zk(zk)
                userAuthorize.save()
                with open('output.txt', 'a') as output:
        output.writeline('Authorized To All Doors') 
        
    except Exception as ex:
        with open('output.txt', 'a') as output:
        output.writeline(ex)
        with open('output.txt', 'a') as output:
        output.writeline('TRY #2')
        try:
            autorized = False
            with ZKAccess(connstr=connstr, device_model=ZK200) as zk:
                user = User(card=card, pin=pin, start_time=datetime.now(), end_time=datetime(9999, 12, 31, 23, 59, 59),
                            super_authorize=False).with_zk(zk)
                user.save()
                # zk.aux_inputs.events.refresh()
                # zk.aux_inputs[0:3].events.poll()
                with open('output.txt', 'a') as output:
        output.writeline(f"IP: {ip} CARD: {card} ADDED SUCCESS")
        
                for UserAuthorizeRecord in zk.table('UserAuthorize'):
                    if UserAuthorizeRecord.pin == pin:
                        autorized = True
                        with open('output.txt', 'a') as output:
        output.writeline('almost authorized')
                if  autorized == False:
                    userAuthorize = UserAuthorize(pin=pin,timezone_id=1,doors=(True, True, True, True)).with_zk(zk)
                    userAuthorize.save()
                    with open('output.txt', 'a') as output:
        output.writeline('Authorized To All Doors') 
        except Exception as ex:
            with open('output.txt', 'a') as output:
        output.writeline(str(ex))
            return False
    return True



def delete_user(card, pin, ip):
    connstr = f"protocol=TCP,ipaddress={ip},port=4370,timeout=4000,passwd="
    try:
        with ZKAccess(connstr=connstr, device_model=ZK200) as zk:
            user = User(card=card, pin=pin,
                        super_authorize=True).with_zk(zk)
            user.delete()
            # zk.aux_inputs.events.refresh()
            # zk.aux_inputs[0:3].events.poll()
            with open('output.txt', 'a') as output:
        output.writeline(f"IP: {ip} CARD: {card} REMOVED SUCCESS")
    except Exception as ex:
        with open('output.txt', 'a') as output:
        output.writeline('TRY #2')
        try:
            with ZKAccess(connstr=connstr, device_model=ZK200) as zk:
                user = User(card=card, pin=pin,
                            super_authorize=True).with_zk(zk)
                user.delete()
                # zk.aux_inputs.events.refresh()
                # zk.aux_inputs[0:3].events.poll()
                with open('output.txt', 'a') as output:
        output.writeline(f"IP: {ip} CARD: {card} REMOVED SUCCESS ON TRY #2")
        except Exception as ex:
            with open('output.txt', 'a') as output:
        output.writeline(str(ex))
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
        with open('output.txt', 'a') as output:
        output.writeline(str(ex))
        return {}
    return res
