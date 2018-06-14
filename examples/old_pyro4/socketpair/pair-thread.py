# this example uses a background thread to run the daemon in, also works on Windows

import socket
import threading
from Pyro5.compatibility import Pyro4
import Pyro4


# create our own socket pair (server-client sockets that are already connected)
sock1, sock2 = socket.socketpair()


class Echo(object):
    @Pyro4.expose
    def echo(self, message):
        print("server got message: ", message)
        return "thank you"


# create a daemon with some Pyro objectrunning on our custom server socket
daemon = Pyro4.Daemon(connected_socket=sock1)
daemon.register(Echo, "echo")
print("(Pyro daemon running on", daemon.locationStr, ")\n")
daemonthread = threading.Thread(target=daemon.requestLoop)
daemonthread.daemon = True
daemonthread.start()


# create a client running on the client socket
with Pyro4.Proxy("echo", connected_socket=sock2) as p:
    reply = p.echo("hello!")
    print("client got reply:", reply)
    reply = p.echo("hello again!")
    print("client got reply:", reply)
with Pyro4.Proxy("echo", connected_socket=sock2) as p:
    reply = p.echo("hello2!")
    print("client got reply:", reply)
    reply = p.echo("hello2 again!")
    print("client got reply:", reply)

print("\nThe end.")
