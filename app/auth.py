from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def fake_decode_token(token: str):
    return {"sub": token}


def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user
