from ..message import Message

def send_command_client(args):
    command = args['command'] 
    if args['result']:
        title = "result"
    else:
        title = None

    message = Message(title=title, content=command)
    return message


def send_mode_server(mess):
    pass
