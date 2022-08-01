from fastapi import FastAPI

from routes.bureau import bureau
app = FastAPI()
app.include_router(bureau, prefix='/bureau')





