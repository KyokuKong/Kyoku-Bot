import os
import sys
from trace import Trace

import sqlalchemy
import sqlite3
from pydantic import constr
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.exc import SQLAlchemyError
from nonebot.log import logger
from websockets import connect

from ..core.config import config
from ..entity import Base, BotUser


class BotDatabase:
    engine: sqlalchemy.Engine
    """
    用于和bot的数据库进行连接和交互的类
    """
    def __init__(self):
        # self.create_connection()
        pass

    def create_connection(self, db_url=""):
        """
        用于和数据库建立连接的函数\n
        自动根据配置文件设置的db类型建立连接，也可以手动传入dburl来进行连接\n
        :return: sqlalchemy的数据库引擎类型
        """
        # 定义用于生成url的函数
        def generate_url() -> str:
            # 检测pyproject中的数据库配置是否合理
            if not config.db_type or config.db_type not in ["postgresql", "mysql", "sqlite"]:
                # 如果结果为“”那么报错并跳出程序
                logger.error(f"传入的数据库类型不合理：{str(config.db_type)}，其应为postgresql，mysql，sqlite中的一个")
                sys.exit()
            # 合理的情况下根据数据库类型来生成对应的数据库访问url
            logger.info(f"当前使用的数据库类型为：{config.db_type}，正在尝试与数据库建立连接...")
            database_url = ""
            if config.db_type == "postgresql":
                database_url = f"postgresql+psycopg2://{config.db_username}:{config.db_passwd}@{config.db_host}:{config.db_port}/kyokubotdb"
            elif config.db_type == "mysql":
                database_url = f"mysql+pymysql://{config.db_username}:{config.db_passwd}@{config.db_host}:{config.db_port}/kyokubotdb"
            elif config.db_type == "sqlite":
                # 检测是否存在保存数据库的文件夹，如果不存在则创建
                if not os.path.exists("databases"):
                    os.mkdir("databases")

                database_url = "sqlite:///databases/kyokubotdb.db"
            return database_url

        # 检测及生成数据库的访问url
        if not db_url:
            db_url = generate_url()

        # 尝试和数据库建立连接
        try:
            # 创建数据库引擎
            # print(db_url)
            engine = create_engine(db_url)
            # 尝试连接数据库
            connection = engine.connect()
            logger.success("成功和kyokubotdb数据库建立连接！")
            # 检测数据表是否存在，不存在则新建表
            if not engine.dialect.has_table(connection, "bot_user"):
                try:
                    logger.warning("数据库中不存在用户数据表，将进行数据库初始化！")
                    Base.metadata.create_all(engine)
                    logger.success("用户数据初始化成功！")
                except sqlalchemy.exc.ProgrammingError as e:
                    logger.error("初始化用户数据时出现了错误：" + str(e))
                    logger.error("如果使用的数据库类型为postgresql，这可能是因为没有授予对应模式的权限导致的")
            # 关闭连接，将engine存储进类中
            connection.close()
            self.engine = engine

        except sqlalchemy.exc.OperationalError as e:
            # 捕获异常并结束进程
            logger.error("数据库连接时发生了错误，请检查网络连接及数据库配置！")
            logger.error(str(e))
            sys.exit()


# 启动单例
botdb = BotDatabase()
