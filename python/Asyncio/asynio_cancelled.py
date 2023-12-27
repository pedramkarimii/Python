# example 1:
import asyncio
from asyncio import CancelledError

async def test(argoman):
    # await asyncio.sleep(3)
    await asyncio.sleep(6)
    print(f"Testing argoman: {argoman}")

async def main():
    # Create a task for the test function
    a = asyncio.create_task(test("pedram"))
    
    # Check if the task is done in a loop
    secs = 0
    while not a.done():
        print("Task is not finished...")
        await asyncio.sleep(1)
        secs += 1
        if secs == 5:
            a.cancel()  # Cancel the task after 5 seconds
    
    try:
        await a  # Try to await the task
    except CancelledError:
        print("Task is Cancelled")

asyncio.run(main())

# example 2:
import asyncio
from asyncio import TimeoutError

async def test(argoman):
    await asyncio.sleep(3)
    # await asyncio.sleep(6)
    print(f"Testing argoman: {argoman}")

async def main():
    # Create a task for the test function
    a = asyncio.create_task(test("pedram"))
    
    try:
        # Wait for the task with a timeout
        await asyncio.wait_for(a, timeout=5)
    except TimeoutError:
        print(f"Timed out waiting for {a}")
    
    # Check if the task is canceled
    print(f"Task canceled: {a.cancelled()}")  # Shows True or False

asyncio.run(main())

# example 3:
import asyncio
from asyncio import TimeoutError

async def test(argoman):
    # await asyncio.sleep(3)
    await asyncio.sleep(6)
    print(f"Testing argoman: {argoman}")

async def main():
    # Create a task for the test function
    a = asyncio.create_task(test("pedram"))
    
    try:
        # Wait for the task with a timeout and shield it
        await asyncio.wait_for(asyncio.shield(a), timeout=5)
    except TimeoutError:
        print("Task is taking longer than expected, but we are working on it")
        await a  # Continue waiting for the task

asyncio.run(main())

