from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, staff, checks, product
#from routers.auth import get_current_active_user, User
from db.base import engine
from db import models


#from sqlalchemy.sql.sqltypes import DateTime
#from schemas import MyDateTime

app = FastAPI(
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.include_router(auth.router)
app.include_router(checks.router)
#app.include_router(staff.router)
app.include_router(product.router)

#@app.get("/secret/", tags=["main"])
#async def read_secret(current_user: User = Depends(get_current_active_user)):
#    return {"secret": "Sarometz ne podliy"}
#

models.Base.metadata.create_all(engine)

