import nonebot
from nonebot.adapters.onebot.v11 import Adapter
from .core.config import config


def start_bot():
    # 初始化 NoneBot
    nonebot.init(
        host=config.onebot_host,
        port=config.onebot_port,
        driver=config.driver
    )

    # 注册适配器
    driver = nonebot.get_driver()
    driver.register_adapter(Adapter)

    # 在这里加载插件
    nonebot.load_builtin_plugins("echo")  # 内置插件
    # nonebot.load_plugin("thirdparty_plugin")  # 第三方插件
    nonebot.load_plugins("kyokubot/plugins/breaked")  # 本地插件

    # 运行Bot
    nonebot.run()


if __name__ == "__main__":
    pass
