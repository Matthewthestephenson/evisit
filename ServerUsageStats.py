from heapq import heappop, heappush, heapify
from datetime import datetime
import random


class int_ip_pair:
    def __init__(self, f, ip_addr):
        self.freq = f
        self.ip = ip_addr

    def __lt__(self, other):
        return self.freq < other.freq


class ServerUsageStats:
    def __init__(self):
        self.visitors_ip_freq = {}
        self.max_heap = []

    '''
    Assume a valid IP Address
    '''
    def request_handled(self, ip):
        if ip not in self.visitors_ip_freq:
            '''
            This is a new visitor IP.  
            Add it to the heap and our dict/map.
            '''
            freq_ip = int_ip_pair(1, ip)
            self.visitors_ip_freq[ip] = freq_ip
            heappush(self.max_heap, freq_ip)

        else:
            '''
            We got another request from the same ip address.
            We need to update the value and update the heap
            '''
            self.visitors_ip_freq[ip].freq += 1
            heapify(self.max_heap)
            print("Collision")

    def clear(self):
        self.visitors_ip_freq = {}
        self.max_heap = []

    def top100(self):
        ips = []
        removed = []
        i = 0
        while self.max_heap and i < 100:
            removed.append(heappop(self.max_heap))
            ips.append(removed[-1].ip)
            i += 1

        for pair in removed:
            self.max_heap.append(pair)

        heapify(self.max_heap)

        return ips

    def get_size(self):
        return len(self.max_heap)


if __name__ == '__main__':
    random.seed()
    s = ServerUsageStats()
    while s.get_size() < 20000000:
        first_octet = random.randrange(255)
        second_octet = random.randrange(255)
        third_octet = random.randrange(255)
        fourth_octet = random.randrange(255)

        ip = str(first_octet) + ":" + str(second_octet)   + ":" + str(third_octet) + ":" + str(fourth_octet)

        now = datetime.now().time()
        print("before request: ", now, "size: ", s.get_size())
        s.request_handled(ip)
        now = datetime.now().time()
        print("after request: ", now, "size: ", s.get_size())

        now = datetime.now().time()
        print("before top 100: ", now, "size: ", s.get_size())
        s.top100()
        now = datetime.now().time()
        print("after top 100: ", now, "size: ", s.get_size())

        print("ip: ", ip, "new size: ", s.get_size())
        print("++++++++++++++++++++++++++++++++++++++++++")
