# Bot的全局入口脚本
# 运行这个脚本会自动对环境进行自检以及生成各种配置文件
# 导入模块
import sys
import os
import tomllib
from nonebot.log import logger, logger_id, default_format, default_filter
from kyokubot.core.config import config
from kyokubot.utils.gradient import gradient_text
from kyokubot.sqls import botdb
from kyokubot.bot import start_bot


# 主函数
def main():
    # 覆写日志输出格式
    logger.remove(logger_id)
    # 添加新的日志处理器
    logger.level("DEBUG", icon=f"*️⃣DDDEBUG")
    logger.level("INFO", icon=f"ℹ️IIIINFO")
    logger.level("SUCCESS", icon=f"✅SUCCESS")
    logger.level("WARNING", icon=f"⚠️WARNING")
    logger.level("ERROR", icon=f"⭕EEERROR")
    logger.add(
        sys.stdout,
        level=0,
        diagnose=True,
        format="<b><lvl>|</lvl></b> <c>{time:MM-DD HH:mm:ss}</c> [<lvl>{level.icon}</lvl>] {message}",
        filter=default_filter
    )
    logger.info("正在读取项目配置文件...")

    # poetry环境检测
    if not os.path.exists("pyproject.toml"):
        logger.error("没有在运行目录中检测到pyproject.toml配置文件！")
        logger.error("Kyoku Bot使用Poetry工具进行依赖管理！请确保在正确安装了Poetry工具后使用poetry run start命令进行启动！")
        sys.exit()
    # 在配置文件存在的情况下尝试读取配置文件并测试合理性
    config.read()
    if config.version == "error":
        logger.error("Poetry环境配置有误！请检查pyproject.toml文件是否正确配置！")
        sys.exit()
    logger.success("配置文件读取成功。")
    logger.info(gradient_text(f"Welcome to Kyoku Bot！当前版本：Beta {config.version}", "74ebd5", "ACB6E5"))

    # 检测SQL连接
    botdb.create_connection()

    # 启动Bot
    logger.info("正在启动Nonebot...")
    start_bot()
