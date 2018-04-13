import sys

sys.path.insert(0, "..")
import time

from opcua import ua, Server

if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://127.0.0.1:7040/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, "MyObject")
    myvar = myobj.add_variable(idx, "MyVariable", 7)
    myvar.set_writable()  # Set MyVariable to be writable by clients

    # starting!
    server.start()
    root = server.get_root_node()
    try:
        count = 0
        while True:
           #time.sleep(1)
           # count += 0.1
            #myvar.set_value(count)
            print(server.get_node(myvar).get_value())
    finally:
        # close connection, remove subcsriptions, etc
        server.stop()