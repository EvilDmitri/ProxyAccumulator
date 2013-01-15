__author__ = 'dmitri'



class Proxy():
    """Class to hold a proxy data, such as ip, port, type"""

    def __init__(self, ip=None, port=None, proxy_type=None, date_created = None, date_last_viewed = None):
        self.ip = ip
        self.port = port
        self.proxy_type = proxy_type
        self.date_created = date_created
        self.date_last_viewed = date_last_viewed



