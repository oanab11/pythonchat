
from optparse import OptionParser

from client.client import Client

PORT=69

if __name__ == "__main__":
    parser=OptionParser()
    parser.add_option("-c","--client",dest="client",help="run in client mode",action="store_true")
    parser.add_option("-i",dest="ip",metavar="IP",help="ip required for client mode")
    parser.add_option("-u","--username",dest="username",metavar="USERNAME",help="the username seen by the other client")

    (options,args)=parser.parse_args()

    if options.username== None:
        print("Missing argument: the username is required")
        exit()
    if options.client==True:
        if options.ip==None:
            print("Missing argument: you have to supply the server ip")
            exit()
        Client(options.ip,PORT,options.username)
    else:
        pass