import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, "100.114.64.87", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())