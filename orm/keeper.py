__author__ = 'dmitri'



from proxy import Proxy
import Queue


class Keeper():
    """Holding list of lists of proxy"""

    def __init__(self, proxy_list=None):
        if not proxy_list:
            self.proxy_queue = Queue.Queue()



