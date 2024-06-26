import os
import sys
from pathlib import Path

_frozen_program = getattr(sys, "frozen", False)
_appdata_local_folder = os.getenv("LOCALAPPDATA")

# source code root path
_source_root = sys._MEIPASS if _frozen_program else Path(os.path.dirname(os.path.abspath(__file__))).parent

# user data root path
_user_data_root = Path(_appdata_local_folder) / "record_tool" if _appdata_local_folder else _source_root

# user run path
_run_root = os.path.dirname(sys.executable) if _frozen_program else _source_root


def expand_source_root(p=None):
    return Path(_source_root) / p if p else Path(_source_root)


def expand_user_data_root(p=None):
    return Path(_user_data_root) / p if p else Path(_user_data_root)


def expand_run_root(p=None):
    return Path(_run_root) / p if p else Path(_run_root)
