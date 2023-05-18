from sqlalchemy import (Column, Integer, String, Float, create_engine)
from sqlalchemy.orm import Session, declarative_base

engine = create_engine('sqlite:///otc.db')

Base = declarative_base()

class Otc(Base):
    __tablename__ = 'otc'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    category = Column(String())
    price = Column(Float())

    def __repr__(self):
        return f'Name:{self.name} Category:{self.category} Price:{self.price}'
        # return f'Otc:' + \
        #     f'name={self.name}, ' + \
        #     f'price={self.price})'

if __name__ == '__main__':
    engine = create_engine('sqlite:///otc.db')
    
    Base.metadata.create_all(engine)