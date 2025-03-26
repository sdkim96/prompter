from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


Base = declarative_base()

class BaseStore:

    class Prompt(Base):
        __tablename__ = 'prompt'

        id = Column(Integer, primary_key=True)
        prompt = Column(String, nullable=False)
        created_at = Column(DateTime, default=datetime.now)
        updated_at = Column(DateTime, default=datetime.now)

        def __repr__(self):
            return f'<Prompt {self.id} {self.prompt}>'
        

    class Completion(Base):
        __tablename__ = 'completion'

        id = Column(Integer, primary_key=True)
        completion = Column(String, nullable=False)
        created_at = Column(DateTime, default=datetime.now)
        updated_at = Column(DateTime, default=datetime.now)

        def __repr__(self):
            return f'<Completion {self.id} {self.completion}>'
        

    def __init__(
        self,
        session: Session,
        
    ) -> None:
        
        self.session = session

        self.__post_init__()
        
    def __post_init__(self):
        Base.metadata.create_all(self.session.bind)
        