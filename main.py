from mcws import MCWS
import websockets
import asyncio

if __name__ == '__main__':
    port = 26367
    server = MCWS()
    start_server = websockets.serve(server.start, "0.0.0.0", port)
    print('请在MC中输入命令：/connect 127.0.0.1:'+str(port))

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
