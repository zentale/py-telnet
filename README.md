# py-telnet

Simple package to read traffic from a telnet server, and also be able to send messages.

You can try stuff out with running netcat, and calling the scripts:

```bash
netcat -l 1025 # on tab1
python tnet.py # on tab2
# every line you enter on tab1, will be received on tab2

python tnet-sub.py
# lets say you enter these on tab1:
# <empty line> : only the "" pattern subscriber will receive
# random text : the ".+" and "" pattern subscribers will receive
# GET xy : all 3 subscribers will receive
```