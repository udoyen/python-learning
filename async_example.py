import asyncio

async def task_one():
    await asyncio.sleep(2)
    print("Task One Completed!")
    
async def task_two():
    await asyncio.sleep(1)
    print("Task Two Completed!")
    
# Create an event loop
loop = asyncio.get_event_loop()



# Run tasks using the created loop
try:
    loop.run_until_complete(asyncio.gather(task_one(), task_two()))
finally:
    loop.close()
    
    