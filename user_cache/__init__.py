from pathlib import Path
from const import USERS_CACHE_DIR, CACHE_DIR, USERS_CACHE_FILE
from ldap3 import Connection, LDIF


def init_cache():
    if not Path.exists(CACHE_DIR):
        Path(CACHE_DIR).mkdir(mode=0o700)

    if not Path.exists(USERS_CACHE_DIR):
        Path(USERS_CACHE_DIR).mkdir(mode=0o700)

    write_ldif()


def write_ldif():
    conn = Connection(None, client_strategy=LDIF)
    conn.stream = open(USERS_CACHE_FILE, 'w')
    with conn:
        conn.delete('cn=test1,o=test')
        conn.delete('cn=test2,o=test')



