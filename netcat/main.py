from .netcat import Server, Client
import socket
import argparse
from .netcat.utils import convert_sys_arg_to_dict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('host')
    parser.add_argument('port', type=int)
    parser.add_argument('-s', '--server', action='store_true')
    parser.add_argument('-e', '--execute')
    parser.add_argument('-S', '--send', nargs='+')
    parser.add_argument('-r', '--result', action='store_true')
    parser.add_argument('-u', '--upload')
    parser.add_argument('-d', '--download')
    args = parser.parse_args()

    if args.server:
        server = Server(args.host, args.port)
        server.run()
    else:
        dict_args = convert_sys_arg_to_dict(args)
        client = Client(args.host, args.port, dict_args)
        client.run()

if __name__ == "__main__":
    main()
