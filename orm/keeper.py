__author__ = 'dmitri'



from proxy import Proxy
import Queue


class Keeper():
    """Holding list of lists of proxy"""

    def __init__(self, proxy_list=None):
        """Initialize keeper"""

        '''proxy_queue = self.load()'''
        proxy_queue = Queue.Queue()
        if not proxy_list:
            self.proxy_queue = Queue.Queue()
        proxy_queue.put(proxy_list)

    def save(self, proxy_list, proxy_type='socks5', file_name="data/proxies.db"):
        """Save list of proxies in to the file
        """

        with open(file_name, 'a') as f:
            for proxy in proxy_list:
                f.write(Proxy.get_data() + '\n')




    def load(self, file_name="data/proxies.db", proxy_list=None, proxy_type=None):
        """Load Proxy[ip, port, proxy_type] from file"""

        if not proxy_list:
            self.proxy_list = []

        with open(file_name, 'r') as f:
            for line in f.readline():
                (ip, port, proxy_type) = line.split()
                proxy = Proxy(ip, port, proxy_type)
                self.proxy_list.append(proxy)

        return proxy_list



