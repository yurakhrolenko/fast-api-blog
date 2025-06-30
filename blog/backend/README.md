Ось **приклад файлової структури FastAPI-проєкту** зі стандартним CRUD для `users`, `posts` та базовими маршрутами авторизації (`/auth/login`, `/auth/register`, `/auth/me`).

---

## 📂 **Файлова структура проєкту (Domain-first)**

```
myproject/
├── app/
│   ├── main.py
│   ├── core/                  # Налаштування, безпека
│   │   ├── config.py
│   │   ├── security.py
│   │   └── database.py
│   ├── api/
│   │   ├── deps.py
│   │   └── v1/
│   │       ├── auth.py
│   │       ├── users.py
│   │       └── posts.py
│   ├── users/
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── services.py
│   │   └── crud.py
│   ├── posts/
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── services.py
│   │   └── crud.py
│   └── auth/
│       ├── schemas.py
│       └── services.py
├── tests/
│   ├── test_auth.py
│   ├── test_users.py
│   └── test_posts.py
├── .env
├── requirements.txt
└── alembic/
    └── ... (міграції)
```

---

## 🔧 Короткий опис основних компонентів:

### `main.py`

```python
from fastapi import FastAPI
from app.api.v1 import auth, users, posts

app = FastAPI(title="MyProject API")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
```

---

### `users/models.py`

```python
from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
```

---

### `users/schemas.py`

```python
from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True
```

---

### `users/crud.py`

```python
def create_user(db: Session, user_in: UserCreate) -> User:
    hashed_pw = hash_password(user_in.password)
    user = User(email=user_in.email, hashed_password=hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
```

---

### `auth/services.py`

```python
def authenticate_user(db, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
```

---

### `api/v1/auth.py`

```python
from fastapi import APIRouter, Depends
from app.auth.schemas import LoginRequest
from app.auth.services import authenticate_user
from app.api.deps import get_db

router = APIRouter()

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    ...
```

---

### `core/database.py`

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
```

---

## 📌 Чому це зручно:

| Перевага            | Пояснення                                                                |
| ------------------- | ------------------------------------------------------------------------ |
| 🌱 Масштабованість  | Легко додати `comments`, `categories`, тощо                              |
| 🧪 Тестованість     | Кожна сутність ізольована — легко писати юніт-тести                      |
| 🔍 Прозорість       | Роутінг, логіка, моделі — розділено                                      |
| ♻️ Перевикористання | `get_db()`, `get_current_user()` — в `deps.py` і підключаються у роутери |

---

🔁 Хочеш, щоб я згенерував тобі готовий шаблон цього проєкту (як cookiecutter), або завантажуваний zip — просто скажи.
