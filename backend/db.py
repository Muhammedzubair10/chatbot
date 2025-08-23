from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from backend.config import DATABASE_URL



engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    with engine.begin() as conn:
        with open("schema.sql") as f:
            conn.execute(text(f.read()))
