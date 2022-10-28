from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from auth import *

router = APIRouter()


@router.post("/auth/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    session = Session(engine)

    email = form_data.username

    user = authenticate_user(session, email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/auth/profile", response_model=schemas.User)
async def get_profile(current_user: schemas.User = Depends(get_admin_user)):
    return current_user
