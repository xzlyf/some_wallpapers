import os

from core import wallhaven_api


# 初始化缓存目录
def init_dir():
    default_save_path = "./save"
    default_cache_path = "./cache"
    if not os.path.exists(default_save_path):
        os.makedirs(default_save_path)
    if not os.path.exists(default_cache_path):
        os.makedirs(default_cache_path)


init_dir()
wallhaven_api.get_random(1)
