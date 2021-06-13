from pathlib import Path


CACHE_DIR = Path.joinpath(Path.home(), '.py_cache')
USERS_CACHE_DIR = Path.joinpath(CACHE_DIR, 'user_cache')
USERS_CACHE_FILE = Path.joinpath(USERS_CACHE_DIR, 'user_cache')
