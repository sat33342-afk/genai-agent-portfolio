import asyncio
import time

async def coverage_check():
    await asyncio.sleep(1)
    return "coverage ok"

async def fraud_check():
    await asyncio.sleep(2)
    return "fraud ok"

async def document_check():
    await asyncio.sleep(1)
    return "documents ok"

async def main():
    start = time.time()
    results = await asyncio.gather(coverage_check(), fraud_check(), document_check())
    print(results)
    print("Time:", round(time.time() - start, 1), "seconds")

asyncio.run(main())