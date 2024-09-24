import os

from .path import expand_source_root, expand_user_data_root

log_path = expand_user_data_root("log")
root_path = expand_user_data_root()
# 用户情报目录
user_info_path = expand_user_data_root("user")
user_info_file = os.path.join(user_info_path, "user_info.json")
default_user_info_file = os.path.join(user_info_path, "default_user_info.json")
# 资源文件目录
resource_path = expand_source_root("resource")
