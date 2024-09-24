import logging


class CustomFormatter(logging.Formatter):
    def format(self, record):
        original_msg = record.getMessage()
        # 获取额外的日志参数
        if hasattr(record, "extra_param"):
            extra_param = record.extra_param
            # 拼接两个参数
            record.msg = f"{original_msg}: {extra_param}"

        # 使用默认的格式化方法
        formatted = super().format(record)

        # 恢复原始记录，以便下次使用
        # record.msg = original_msg

        return formatted


def log(level, label="", message=""):
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


# 创建一个logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()

console_handler.setLevel(logging.DEBUG)

# 定义handler的输出格式
formatter = CustomFormatter("|%(asctime)s| %(levelname)-7s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
# logger.info("info", "This is an info message", "Additional information")
log("info", "登录", "登录成功")
log("info", "登录", "登录失败")
