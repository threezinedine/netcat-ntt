import json
from .message import Message


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

        return lambda x: x + 1, self._mode_mess, 

    def get_mode(self, mode_mess):
        print(type(mode_mess.get_content()), mode_mess.get_content())
        self._args = json.loads(mode_mess.get_content())
        return lambda x: -1
