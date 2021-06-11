from ldap3 import Server, Connection, ALL, SUBTREE


def has_attr(entry, attr_name):
    return attr_name.lower() in list(map(lambda x: x.lower(), entry.entry_attributes))


server = Server('localhost', port=1389, get_info=ALL)
conn = Connection(server, user="cn=Directory Manager", password="1qwertyu")
if not conn.bind():
    print('error in bind: ', conn.result)

conn.search('ou=People,dc=example,dc=com', '(uid=user.1000)', SUBTREE, attributes=['*'])
for entry in conn.entries:
    # print(entry.entry_definition)
    # print(entry.entry_raw_attributes)
    # print(entry.entry_to_ldif())
    # print(type(entry))
    # print(type(entry.cn))
    # print('userpassword' in entry.entry_attributes)
    # print(entry.entry_raw_attributes)
    print(has_attr(entry, 'userPassword'))
    print(has_attr(entry, 'displayName'))
