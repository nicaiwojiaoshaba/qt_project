import logging
import os

from logging.handlers import RotatingFileHandler
from .config import log_path

_logger_instance = None


class CustomFormatter(logging.Formatter):
    def format(self, record):
        original_msg = record.getMessage()

        # 获取额外的日志参数
        if hasattr(record, "extra_param"):
            extra_param = record.extra_param
            # 拼接两个参数
            record.msg = f"[{original_msg}] {extra_param}"

        # 使用默认的格式化方法
        formatted = super().format(record)

        # 恢复原始记录，以便下次使用
        record.msg = original_msg

        return formatted


"""
创建log文件日志格式
    |2024-09-13 11:18:56| INFO    | 注册成功，跳转到登录界面
"""
FILE_FORMATTER = CustomFormatter("[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
"""
创建控制台日志格式
    注册成功，跳转到登录界面
"""
CONSOLE_FORMATTER = CustomFormatter("[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")


def get_logger(log_name="record_tool_log", log_level=logging.INFO, log_dir=log_path, max_bytes=1024 * 1024, backup_count=5):
    """
    初始化日志记录器。
    :param log_name: 日志记录器的名字，默认为 'record_tool_log'。
    :param log_level: 日志级别，默认为 INFO。
    :param log_dir: 日志文件保存的目录，默认为当前目录下的 'logs' 文件夹。
    :param max_bytes: 单个日志文件的最大大小（以字节为单位），默认为 5MB。
    :param backup_count: 保留的日志文件数量,默认保留5个log文件。
    """
    global _logger_instance
    if _logger_instance is None:
        # 设置日志目录
        if log_dir is None:
            log_dir = os.path.join(os.getcwd(), "logs")
        os.makedirs(log_dir, exist_ok=True)

        # 创建日志记录器
        logger = logging.getLogger(log_name)
        logger.setLevel(log_level)

        # 创建文件处理器
        log_file_path = os.path.join(log_dir, f"{log_name}.txt")
        handler = RotatingFileHandler(log_file_path, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8")
        handler.setLevel(log_level)
        handler.setFormatter(FILE_FORMATTER)

        # 将文件处理器添加到记录器
        if not logger.hasHandlers():
            logger.addHandler(handler)

        # 添加控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(CONSOLE_FORMATTER)
        logger.addHandler(console_handler)

        _logger_instance = logger

    return _logger_instance


logger = get_logger()


def LOG(level, label, message):
    if level == "info":
        logger.info(label, extra={"extra_param": message})
    elif level == "debug":
        logger.debug(label, extra={"extra_param": message})
    elif level == "warning":
        logger.warning(label, extra={"extra_param": message})
    elif level == "error":
        logger.error(label, extra={"extra_param": message})
    elif level == "critical":
        logger.critical(label, extra={"extra_param": message})


class LEVEL:
    INFO = "info"
    DEBUG = "debug"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"
