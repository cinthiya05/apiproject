from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import sessionmaker

# Database configuration (change these with your credentials)
from urllib.parse import quote_plus

DB_USER = "root"
DB_PASSWORD = quote_plus("Cinthiya@30") 
DB_HOST = "localhost"
DB_NAME = "school"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)

# Create the table (optional if already created in DB)
Base.metadata.create_all(bind=engine)

# Pydantic model
class StudentCreate(BaseModel):
    id: int
    name: str
    email: str

app = FastAPI()

# POST endpoint to insert a student
@app.post("/students/")
def create_student(student: StudentCreate):
    db = SessionLocal()
    db_student = Student(id=student.id, name=student.name, email=student.email)
    try:
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return {"message": "Student added", "student": student}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "world"}
