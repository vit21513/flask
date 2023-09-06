from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str = 'sqlite:///mydatabase.db'

    class Config:
        env_file = '.env'


settings = Settings()


app.include_router(user.router, tags=["users"])

router = APIRouter()


@router.get("/users", response_model=list[User])