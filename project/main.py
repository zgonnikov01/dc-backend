from fastapi import Depends, FastAPI
from routers import auth
from routers.auth import get_current_active_user, User


app = FastAPI()
app.include_router(auth.router)

@app.get("/secret/")
async def read_secret(current_user: User = Depends(get_current_active_user)):
    return {"secret": "Sarometz ne podliy"}
