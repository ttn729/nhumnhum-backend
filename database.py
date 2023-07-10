from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database connection URL
DATABASE_URL = "sqlite:///./database.db"

# Create the SQLAlchemy engine and session
engine = create_engine(DATABASE_URL, pool_size=10, pool_recycle=3600)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base model
Base = declarative_base()


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    collection = Column(String)
    question = Column(String)
    type = Column(String)
    prompt = Column(String, nullable=True)
    op1 = Column(String, nullable=True)
    op2 = Column(String, nullable=True)
    op3 = Column(String, nullable=True)
    op4 = Column(String, nullable=True)
    answer = Column(String)

# Create the database tables
def create_tables():
    Base.metadata.create_all(bind=engine)
