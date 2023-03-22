import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        if str(message).startswith('1'):
            await websocket.send("Here is a 1")
        if str(message).startswith('a'):
            await websocket.send("Here is a a")
        else:
            await websocket.send(message)
async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())

