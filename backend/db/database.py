import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv

load_dotenv()

mode = (os.getenv("DB_CONNECTION_MODE") or "direct").lower()

if mode == "pooled_tx":
    # Use the pooler URL and disable SQLAlchemy's own pooling (avoid double pooling)
    DATABASE_URL = os.getenv("DATABASE_URL_POOLED_TX")
    engine = create_engine(
        DATABASE_URL,
        poolclass=NullPool,      # let Supabase pooler do the pooling
        pool_pre_ping=True,      # safe check for stale conns
    )
else:
    # Direct connection with modest pool for FastAPI
    DATABASE_URL = os.getenv("DATABASE_URL_DIRECT")
    engine = create_engine(
        DATABASE_URL,
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True,
        pool_recycle=1800,       # refresh every 30 min to avoid stale conns
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
