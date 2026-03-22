import sys
from loguru import logger

def setup_logger(log_file: str = "app.log", level: str = "INFO"):
    """
    配置并初始化 loguru 日志记录器
    
    参数:
        log_file: 日志文件存储路径
        level: 日志级别 (如 'INFO', 'DEBUG', 'WARNING')
    """
    # 移除默认的接收器以避免重复输出
    logger.remove()
    
    # 配置文件写入接收器，每天轮转一次，保留一周的日志
    logger.add(
        log_file,
        rotation="1 day",
        retention="7 days",
        level=level,
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
        enqueue=True, # 异步安全
    )
    
    # 配置控制台标准输出接收器，具有丰富的色彩显示
    logger.add(
        sys.stderr,
        level=level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    )

    logger.debug("Logger initialized and configured successfully.")
    return logger
