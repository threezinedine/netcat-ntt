import json


class Message:
    header_size = 10

    def __init__(self, msg=None, type_msg=None, b_msg=None):
        self._dic = {}
        self._encoded_msg = None

        if msg is not None or type_msg is not None:
            self._set_msg(msg)
            self._set_title(type_msg)
            self._encode()
        else:
            self._decode(b_msg)

    def _set_msg(self, msg):
        if msg is None: 
            msg = ""
        self._dic["content"] = msg

    def _set_title(self, type_msg):
        if type_msg is None:
            type_msg = ""
        self._dic["type"] = type_msg

    def _create_header_msg(self, dumped_dict):
        len_msg = len(dumped_dict)
        header_msg = f"{len_msg}"

        while len(header_msg) < self.header_size:
            header_msg += " "
        return header_msg

    def _encode(self):
        dumped_dict = json.dumps(self._dic) 
        header_msg = self._create_header_msg(dumped_dict)
        self._encoded_msg = (header_msg + dumped_dict).encode("utf-8")

    def _decode(self, b_msg):
        self._dic = json.loads(b_msg.decode("utf-8"))
        self._encode()

    def get_message(self):
        return self._dic["content"] 

    def get_message_type(self):
        return self._dic["type"]

    def get_encoded_message(self):
        return self._encoded_msg
