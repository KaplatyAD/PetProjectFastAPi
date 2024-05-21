import uvicorn
from fastapi import FastAPI
from .web import explorer, creature

app = FastAPI()
app.include_router(explorer.router)
app.include_router(creature.router)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app, reload=True)
