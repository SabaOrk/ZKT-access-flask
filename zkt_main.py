from zk import ZK, const

conn = None
# create ZK instance
zk = ZK('149.3.34.69', port=4370)
try:
    # connect to device
    conn = zk.connect()
except Exception as ex:
    print(ex)