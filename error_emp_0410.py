import logging

logging.basicConfig(filename='./error_emp_log.log',level=logging.INFO,format="%(asctime)s [line:%(lineno)d] %(message)s")

class InvaidInputException(Exception):
    def __init__(self, message):
        super(InvaidInputException, self).__init__(message)
        self.message = message


class DependException(Exception):
    def __init__(self, message):
        super(DependException, self).__init__(message)
        self.message = message


class InternalException(Exception):
    def __init__(self, message):
        super(InternalException, self).__init__(message)
        self.message = message


hot = ['paper', 'fish', 'brash', 'oil']
u_dct = {
    1: ['game mouse', 'game jianpan'],
    2: ['kou hong', 'xiang shui']
}
geo_dct = {
    '1_1': ['huo guo', 'la jiao'],
    '1_2': ['san wen yu', 'ba jiao'],
    '1_3': ['black pip', 'good meat']
}


def getData(uid, jid, wid):
    u_val,g_val = [], []
    try:
        u_val = u_dct[uid]
    except Exception as e:
        logging.error('get u_val error: %s' % e)
    try:
        g_val = geo_dct['%d_%d' % (jid, wid)]
    except Exception as e:
        logging.error('get g_val error: %s' % e)
    res = hot + u_val + g_val
    return res


def getWebsite(uid, jid, wid):
    res = []
    try:
        res = getData(uid, jid, wid)
    except Exception as e:
        logging.error('getData error: %s' % e)
    return {uid: res, 'status': 200}


if __name__ == "__main__":
    res = 'error'
    try:
        res = getWebsite(1, 1,2)
    except Exception as e:
        logging.error('getWebsite error: %s' % e)
    logging.info(res)