__author__ = 'dmitri'

# /usr/bin/env/python
# -*-coding=utf-8-*-

import grab

g = grab.Grab()

g.go("http://2ip.ru/")

real_ip =  g.xpath_text( '//big[@id="d_clip_button"]')
print "real_ip - %s" % real_ip

#g.setup(proxy='gate.somhost.com:444', proxy_type='http')

def CheckIp():
    good_ip_list = []
    with open('../data/ip-port.txt') as f:
        ip_list = f.readlines()

    for stroke in ip_list:
        type_sock, ip, port = stroke.split()

        print 'Will try - % s' % stroke
        g.setup(proxy=':'.join([ip, port]), proxy_type=type_sock)
        try:
            g.go("http://2ip.ru/")
            fake_ip =  g.xpath_text( '//big[@id="d_clip_button"]')
            if real_ip != fake_ip:
                good_ip_list.append(fake_ip)

        except grab.error.GrabError:
            pass

    return good_ip_list



if __name__ == '__main__':
    CheckIp()