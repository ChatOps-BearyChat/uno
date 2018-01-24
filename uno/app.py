# -*- coding: utf-8 -*-

import time

from bearychat import RTMClient

from uno.client import Client
from uno.rtm_loop import RTMLoop


class UNO(object):

    def __init__(self, token):
        self.commands = dict()
        self.token = token
        self.client = Client(token)

    def register_command(self, command):
        if command.name in self.commands:
            raise ValueError('Command %s has been registered' % command.name)

        self.commands[command.name] = command

    def dispatch(self, message):
        command = self.get_command_from_message(message)
        if command is None:
            return
        command_handler = self.commands.get(command)
        if command_handler:
            command_handler.execute(self.loop, message)

    def run(self):
        self.rtm_client = RTMClient(self.token, "https://rtm.bearychat.com")
        resp = self.rtm_client.start()
        self.user = resp["user"]

        self.loop = RTMLoop(resp["ws_host"])
        self.loop.start()

        time.sleep(1)

        while True:
            error = self.loop.get_error()
            if error:
                print(error)
                continue
            message = self.loop.get_message(True, 5)

            if not message or not message.is_chat_message():
                continue
            try:
                self.dispatch(message)
                print("rtm loop received {0} from {1}".format(message["text"],
                                                              message["uid"]))
            except Exception as e:
                print e
                continue

            if message.is_from(self.user):
                continue

    def get_command_from_message(self, message):
        if message.is_p2p() :
            command = message['text'].split()[0]
        else:
            command = message['text'].split()[1]
        return command
