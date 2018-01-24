===
UNO
===

Introduction
------------

A ChatOps framework for BearyChat.

Usage
------

::

    from uno import UNO, Command


    uno = UNO('<YOUR_RTM_TOKEN>')
    ping_command = Command('ping')
    uno.register_command(ping_command)


    @ping_command.listen
    def ping(client, message):
        client.send(message.refer('pong'))


    def main():
        uno.run()


    if __name__ == '__main__':
        main()
