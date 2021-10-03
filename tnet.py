from telnetlib import Telnet
from threading import Thread


def reader(tn, update_handle):
    """Reads lines from a telnet connection, sends each received line to update_handle."""
    while True:
        msg = tn.read_until(b"\n", 5)
        if msg:
            update_handle(msg.decode())


class TelnetGateway:
    """Using a single telnet connection, reads updates and sends messages."""

    def __init__(self, host, port):
        self.tn = Telnet(host, port, 5)
        self.reader_thread = Thread(target=reader, args=[self.tn, self._update_handle], daemon=True)
        self.reader_thread.start()

    def _update_handle(self, msg):
        self.update_handle(msg.strip())

    def update_handle(self, msg):
        print(f"Received update: {msg}")

    def send_msg(self, msg):
        self.tn.write(msg.encode() + b"\n")
        print(f"Written: {msg}")


def main():
    gw = TelnetGateway("localhost", 1025)
    print("hello")
    while True:
        m = input("What do you want to send?\n")
        gw.send_msg(m)


if __name__ == "__main__":
    main()
