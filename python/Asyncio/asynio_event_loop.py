import asyncio

# Asynchronous function to simulate a test with a sleep of 2 seconds
async def test(argoman):
    await asyncio.sleep(2)
    print(f"Testing argoman: {argoman}")

# Main asynchronous function to create tasks and wait for their completion
async def main():
    # Create two tasks to run the test function concurrently
    a = asyncio.create_task(test("pedram"))
    b = asyncio.create_task(test("pedram"))
    
    # Wait for the completion of task 'a'
    await a
    
    # Wait for the completion of task 'b'
    await b

# Create a new event loop
loop = asyncio.new_event_loop()

try:
    # Run the main function until it completes
    loop.run_until_complete(main())

finally:
    # Close the event loop
    loop.close()

