from datetime import datetime, timedelta

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel



from secret import SECRET_KEY
from schemas import UserBase, UserDisplay

from sqlalchemy.orm.session import Session
from typing import List

from db import db_user
from db.base import get_db
from db.db_user import get_user

from schemas import Token, TokenData
from hash import Hash
User = UserBase



#SECRET_KEY = "da257a3e4b6595c441ff526c6d6b751a68cf5d1f49b8221ffc87501865ee4b25"


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 1e5


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_users_db = {
    "sarometz": {
        "username": "sarometz",
        "full_name": "Evgeny Andreevich",
        "email": "sarometz@example.com",
        "hashed_password": pwd_context.hash("podliy"),
        "disabled": False,
    }
}


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    tags=["auth"]
)


def authentificate_user(email: str, password: str, db: Session):
    #user = get_user(fake_db, username)
    user = get_user(db, email)
    if not user:
        return False
    if not Hash.verify(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=1e5)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(username=email)
    except JWTError:
        raise credentials_exception
    #user = get_user(fake_users_db, username=token_data.username)
    user = get_user(db, email)
    if user is None:
        raise credentials_exception
    return user


def get_current_active_user(current_user: User = Depends(get_current_user)):
    #if current_user.disabled:
    #    raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def get_user_provider(current_active_user: User = Depends(get_current_active_user)):
    if current_active_user.access_level == -1:
        return current_active_user
    raise HTTPException(status_code=401, detail="Provider rights required")

def get_user_admin(current_active_user: User = Depends(get_current_active_user)):
    if current_active_user.access_level == 9999:
        return current_active_user
    raise HTTPException(status_code=401, detail="Admin rights required")

def get_user_full_access(current_active_user: User = Depends(get_current_active_user)):
    if current_active_user.access_level >= 20:
        return current_active_user
    raise HTTPException(status_code=401, detail="Full access rights required")

def get_user_manager(current_active_user: User = Depends(get_current_active_user)):
    if current_active_user.access_level >= 10:
        return current_active_user
    raise HTTPException(status_code=401, detail="Manager rights required")

def get_user_basic(current_active_user: User = Depends(get_current_active_user)):
    if current_active_user.access_level >= 1:
        return current_active_user
    raise HTTPException(status_code=401, detail="Basic rights required")

#@router.post("/token", response_model=Token, tags=["auth"])
@router.post("/token", tags=["auth"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authentificate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authentificate": "Bearer"},
        )
    access_token_expires = timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    #return {"access_token": access_token, "token_type": "bearer"}
    return {"access_token": access_token}

@router.post("/create_user", response_model=UserDisplay)
async def create_user(
        request: UserBase,
        db: Session = Depends(get_db),
        #user: User = Depends(get_user_admin)
    ):
    return db_user.create_user(db, request)

#@router.post("/get_user", response_model=UserDisplay | None)
#async def get_user(email: str, db: Session = Depends(get_db)):
#    return db_user.get_user(db, email)
    #return db_user.get_all_users(db)[0]

