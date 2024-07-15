from sqlalchemy import create_engine, Column, Integer, String, JSON, Float
from .base import Base


class BotUser(Base):
    """
    定义用户数据实体的ORM类
    """
    __tablename__ = 'bot_user'
    qid = Column(Integer, primary_key=True)
    level = Column(Integer)
    roles = Column(JSON)  # 使用 JSON 存储列表
    points = Column(Float)
    coins = Column(Float)
    crystals = Column(Float)
    register_date = Column(Integer)
    last_sign_date = Column(Integer)
    backpack = Column(String)  # 存储 JSON 字符串数据
