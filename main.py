import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("LANGSMITH_ENDPOINT"))

async def main():
    print("Hello from langchain-mcp-adaptors!")

if __name__ == "__main__":
    asyncio.run(main())
