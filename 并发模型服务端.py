"""
tcp网络并发模型
"""

from socket import *
from threading import Thread

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)


class Mythread(Thread):
    def __init__(self, connfd):
        super().__init__()
        self.connfd = connfd

    def run(self):
        while True:
            data = self.connfd.recv(1024)
            if not data:
                break
            print('Recv:', data.decode())
            self.connfd.send(b'Thanks')
        self.connfd.close()


def main():
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    print('listen the port %s' % PORT)

    while True:
        try:
            connfd, addr = sock.accept()
            print('connect from addr')
        except KeyboardInterrupt:
            sock.close()
            return
        t = Mythread(connfd)
        t.setDaemon(True)
        t.start()


if __name__ == '__main__':
    main()
