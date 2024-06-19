import message_utils
import ref_strings
import midi_player
import os
import json
import websockets
import sys

class WSWrapper:
    def __init__(self,ws) -> None:
        self.ws=ws

    async def send(self,data):
        # print(coloreplace.replace("\u00a71> SEND: \t"+data))
        await self.ws.send(data)

    async def recv(self):
        result = await self.ws.recv()
        # print(coloreplace.replace("\u00a72< RECV: \t"+result))
        return result

class MCWS:

    async def start(self, ws, path):
        self.ws =  WSWrapper(ws)
        self.modules = {}
        self.config = {'stats': {}, 'modules': {}}
        message_utils.log_command = False
        
        await ws.send(message_utils.info(ref_strings.loading))

        
        self.player = midi_player.MidiPlayer(self.ws)
        self.player.start()
        self.modules[self.player.module_id] = self.player

        await self.load_config()
        await self.listen_event()
        await self.hello()
    
    async def listen_event(self):
        # 监听聊天信息
        await self.ws.send(message_utils.sub)

    async def load_config(self):
        if os.path.exists('config.json'):
            with open('config.json') as f:
                self.config = json.loads(f.read())

            for key in self.modules:
                module = self.modules[key]
                try:
                    module.set_config(self.config['modules'][module.module_id])
                except KeyError:
                    module.config = module.default_config
                    continue

                for i in module.default_config:
                    if i not in module.config:
                        module.config[i] = module.default_config[i]

            message_utils.log_command = self.config['debug']
        else:
            for module in self.modules:
                self.modules[module].config = self.modules[module].default_config

        print(self.config)

    def get_config(self):
        for k in self.modules:
            module = self.modules[k]
            try:
                self.config['modules'][module.module_id] = module.config
            except:
                pass
        self.config['debug'] = message_utils.log_command
        return self.config
    
    def save(self):
        self.get_config()
        print(self.config)
        with open('config.json', 'w') as f:
            f.write(json.dumps(self.config))

    
    async def parse_command(self, msg):
        if msg["header"]["messagePurpose"] == "event":
            if msg["header"]["eventName"] == "PlayerMessage":
                # self.log.log(msg)
                raw = message_utils.getChat(msg)
                args = raw.split(" ")

                if args[0] == ".midi":
                    await self.player.parse_command(args[1:])

        elif msg["header"]["messagePurpose"] == "commandResponse":
            pass  
        
    async def hello(self):
        await self.ws.send(message_utils.info(ref_strings.welcome))
        await self.ws.send(message_utils.info(ref_strings.welcome_info))
        # self.log = self.modules['ChatLogger']
        try:
            while True:
                data = await self.ws.recv()
                msg = json.loads(data)
                await self.parse_command(msg)
        except (
                KeyboardInterrupt, websockets.exceptions.ConnectionClosedOK,
                websockets.exceptions.ConnectionClosedError,
                websockets.exceptions.ConnectionClosed):
            self.player.close()
            # self.log.close()
            self.save()
            sys.exit()