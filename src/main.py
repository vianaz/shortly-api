import os

import uvicorn

from dotenv import load_dotenv


load_dotenv()


def main():
    uvicorn.run(
        "src:app",
        host="localhost",
        port=int(int(os.getenv("PORT") or 8000)),
        reload=True,
    )


if __name__ == "__main__":
    main()
