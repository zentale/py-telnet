from tnet import TelnetGateway
import re


class TelnetSubscriber:
    """Subscriber of TelnetGatewayPublisher, receiving only messages of a certain pattern."""

    def __init__(self, pattern):
        self.telnet_pattern = pattern
        self.telnet_callback = lambda x: print(f"<{pattern}> - Received: {x}")


class TelnetGatewayPublisher(TelnetGateway):
    """Publishes received telnet messages matching the pattern required by subscribers."""

    def __init__(self, host, port):
        super().__init__(host, port)
        self.subs = set()

    def subscribe(self, s: TelnetSubscriber):
        self.subs.add(s)

    def unsubscribe(self, s: TelnetSubscriber):
        self.subs.remove(s)

    def update_handle(self, msg):
        for s in self.subs:
            p = re.compile(s.telnet_pattern)
            if p.match(msg):
                s.telnet_callback(msg)


def main():
    subs = [TelnetSubscriber(""), TelnetSubscriber(".+"), TelnetSubscriber("GET .*")]
    gw = TelnetGatewayPublisher("localhost", 1025)
    for s in subs:
        gw.subscribe(s)

    while True:
        m = input("What do you want to send?\n")
        gw.send_msg(m)


if __name__ == "__main__":
    main()