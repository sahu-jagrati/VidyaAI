from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from app.database.connection import Base


class ProcessedFile(Base):
    __tablename__ = "processed_files"

    id           = Column(Integer, primary_key=True, index=True)
    file_name    = Column(String(500), nullable=False, index=True)
    file_hash    = Column(String(64),  nullable=False, unique=True)  # SHA-256 hex
    processed_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
