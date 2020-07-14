import websockets
import requests
import asyncio

async def newEvent():
    uri = 'ws://miac74.ru:9998'
    async with websockets.connect(uri) as websocket:
        eventCount = 0
        while True:
            if eventCount < 200:
                f = open("events.txt", "a")
                event = await websocket.recv()
                f.write(event + '\n')
                f.close()
                eventCount += 1
            else:
                eventCount = 0
                data = []
                f = open("events.txt", "r")
                for line in f:
                    data.append(eval(line))
                requests.post("Тут нужен URL", json = data)
                f.close()
                f = open("events.txt", "w")
                f.write("")
                f.close()

asyncio.get_event_loop().run_until_complete(newEvent())
asyncio.get_event_loop().run_forever()
