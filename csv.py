
user = {}
file = open('passwd.txt', 'r')
for line in file:
    if line.startswith('#') and line.strip():
        user_info = line.split(':')
        user[user_info[0]] = user_info[2]
for username, user_id in sorted(user.items()):
    print(f'{username}: {user_id}')
    