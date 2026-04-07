from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from . import token, database, models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
get_db = database.get_db

def get_current_user(data: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # verify_token returns payload dict like {"user_id": 1}
    payload = token.verify_token(data, credentials_exception)
    
    user_id: int = payload.get("user_id")
    if user_id is None:
        raise credentials_exception
    
    # fetch user from DB
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise credentials_exception
    return user