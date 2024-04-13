import uvicorn

from settings import config_parameters

if __name__ == "__main__":
    if config_parameters.IS_PROD:
        uvicorn.run(
            "setup:server",
            host="0.0.0.0",
            port=80,
            loop="uvloop",
            reload=False,
            use_colors=True,
        )
    else:
        uvicorn.run(
            "setup:server",
            host="0.0.0.0",
            port=80,
            loop="asyncio",
            reload=True,
            use_colors=True,
        )
