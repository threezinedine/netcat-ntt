import json
from .message import Message
from .utils import (send_command_client, send_command_server,
            upload_file_client, upload_file_server,
            download_file_client, download_file_server)


class CommunicateMode:
    def __init__(self):
        self._args = {}
        self._mode_mess = None

    def get_args(self):
        return self._args 

    def get_mode_mess(self):
        return self._mode_mess

    def set_mode(self, args):
        self._args = args 
        self._mode_mess = Message(
                title="mode",
                content=json.dumps(args)
                )

        func = None

        if args['send']:
            func = send_command_client
        elif args['upload']:
            func = upload_file_client
        elif args['download']:
            func = download_file_client

        return func, self._mode_mess, 

    def get_mode(self, mode_mess):
        self._args = json.loads(mode_mess.get_content())
        func = None

        if self._args['send']:
            func = send_command_server 
        elif self._args['upload']:
            func = upload_file_server
        elif self._args['download']:
            func = download_file_server
        return func
