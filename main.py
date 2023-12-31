from pyzkaccess import ZKAccess, ZK200, ZK100, ZK400
from pyzkaccess.tables import User,UserAuthorize
from datetime import datetime
import ping3
import time

connstr = "protocol=TCP,ipaddress=149.3.34.167,port=4370,timeout=10000,passwd="


def ping_host(host):
    try:
        rtt = ping3.ping(host)
        if rtt is not None:
            print(print(f"Ping successful. Round-trip time: {rtt} ms"))
            return('Ping Pass')
        else:
            print('Ping Failed')
            return('Ping Failed')
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def write_log(text):
    with open('log.txt', 'a') as logFile:
        dr = str(datetime.now())+' - '
        text = dr+text
        logFile.write(text)
        logFile.write('\n')
        logFile.close()

def add_user(card, pin, ip, port = 470):
    connstr = f"protocol=TCP,ipaddress={ip},port={port},timeout=4000,passwd="
    try:
        autorized = False
        with ZKAccess(connstr=connstr, device_model=ZK200) as zk:
            user = User(card=card, pin=pin, start_time=datetime.now(), end_time=datetime(9999, 12, 31, 23, 59, 59),
                        super_authorize=False).with_zk(zk)
            user.save()
            # zk.aux_inputs.events.refresh()
            # zk.aux_inputs[0:3].events.poll()
            print(f"IP: {ip} CARD: {card} ADDED SUCCESS")
        
            for UserAuthorizeRecord in zk.table('UserAuthorize'):
                if UserAuthorizeRecord.pin == pin:
                    autorized = True
                    print('almost authorized')
            if  autorized == False:
                userAuthorize = UserAuthorize(pin=pin,timezone_id=1,doors=(True, True, True, True)).with_zk(zk)
                userAuthorize.save()
                print('Authorized To All Doors') 
        
    except Exception as ex:
        print(ex)
        print('TRY #2')
        try:
            autorized = False
            with ZKAccess(connstr=connstr, device_model=ZK200) as zk:
                user = User(card=card, pin=pin, start_time=datetime.now(), end_time=datetime(9999, 12, 31, 23, 59, 59),
                            super_authorize=False).with_zk(zk)
                user.save()
                # zk.aux_inputs.events.refresh()
                # zk.aux_inputs[0:3].events.poll()
                print(f"IP: {ip} CARD: {card} ADDED SUCCESS")
        
                for UserAuthorizeRecord in zk.table('UserAuthorize'):
                    if UserAuthorizeRecord.pin == pin:
                        autorized = True
                        print('almost authorized')
                if  autorized == False:
                    userAuthorize = UserAuthorize(pin=pin,timezone_id=1,doors=(True, True, True, True)).with_zk(zk)
                    userAuthorize.save()
                    print('Authorized To All Doors') 
        except Exception as ex:
            print(str(ex))
            text = str(ex) + '\n'+ping_host(ip)
            write_log(text)
            return False
    return True



def delete_user(card, pin, ip, port = 4370):
    connstr = f"protocol=TCP,ipaddress={ip},port={port},timeout=4000,passwd="
    try:
        with ZKAccess(connstr=connstr, device_model=ZK200) as zk:
            user = User(card=card, pin=pin,
                        super_authorize=True).with_zk(zk)
            user.delete()
            # zk.aux_inputs.events.refresh()
            # zk.aux_inputs[0:3].events.poll()
            print(f"IP: {ip} CARD: {card} REMOVED SUCCESS")
    except Exception as ex:
        print('TRY #2')
        try:
            with ZKAccess(connstr=connstr, device_model=ZK200) as zk:
                user = User(card=card, pin=pin,
                            super_authorize=True).with_zk(zk)
                user.delete()
                # zk.aux_inputs.events.refresh()
                # zk.aux_inputs[0:3].events.poll()
                print(f"IP: {ip} CARD: {card} REMOVED SUCCESS ON TRY #2")
        except Exception as ex:
            print(str(ex))
            text = str(ex) + '\n'+ping_host(ip)
            write_log(text)
            return False
    return True


def get_users(ip, port):
    connstr = f"protocol=TCP,ipaddress={ip},port={port},timeout=4000,passwd="
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
