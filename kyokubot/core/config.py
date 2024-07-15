import tomllib

from nb_cli.config.parser import CONFIG_FILE
from sqlalchemy.testing.plugin.plugin_base import read_config


class Config:
    """
    用于从项目配置文件中获取需要的配置项
    """
    version: str
    onebot_host: str
    onebot_port: int
    driver: str = "~fastapi+~httpx+~websockets"
    db_type: str
    db_host: str
    db_port: int
    db_username: str = "kyokubot"
    db_passwd: str = ""

    def read(self):
        with open("./pyproject.toml", "r", encoding="utf-8") as pyconf:
            conf = tomllib.loads(pyconf.read())
            pyconf.close()
        # 读取配置
        project_config = conf.get("tool", {}).get("poetry", {})
        self.version = project_config.get("version", "error")

        bot_config = conf.get("kyokubot", {}).get("config", {})
        self.onebot_host = bot_config.get("host", "0.0.0.0")
        self.onebot_port = bot_config.get("port", 23333)
        self.db_type = bot_config.get("db_type", "")
        self.db_host = bot_config.get("db_host", "127.0.0.1")
        self.db_port = bot_config.get("db_port", 0)
        self.db_username = bot_config.get("db_username", "kyokubot")
        self.db_passwd = bot_config.get("db_passwd", "")


# 全局单例
config = Config()
