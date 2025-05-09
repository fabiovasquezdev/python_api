from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repository.user import UserRepository
from app.services.user import UserService
from app.schemas.user import User, UserCreate, UserUpdate
from typing import List

router = APIRouter(prefix="/api/users", tags=["users"])

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    user_repository = UserRepository(db)
    return UserService(user_repository)

@router.post("/", response_model=User)
def create_user(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    db_user = user_service.get_user_by_email(user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(user)

@router.get("/", response_model=List[User])
def read_users(user_service: UserService = Depends(get_user_service)):
    return user_service.get_users()

@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    db_user = user_service.get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=User)
def update_user(
    user_id: int,
    user: UserUpdate,
    user_service: UserService = Depends(get_user_service)
):
    db_user = user_service.update_user(user_id, user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}")
def delete_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    success = user_service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"} 