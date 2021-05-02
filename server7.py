import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('localhost', 8070))
serv.listen(5)
users = open("Users.txt", "r")
text = users.readlines()
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        from_client = conn.recv(4096)
        if not from_client: break
        from_client = from_client.decode('utf-8')
        found = False
        user = ''
        counter = 0
        for line in text:
            if from_client in line:
                found = True
                conn.send(("Confirmed").encode('utf-8'))
                user = line
                break
            counter += 1
        if found == False:
            conn.send(("Denied").encode('utf-8'))
            break
        conn.send(("How much money would you like to withdraw").encode('utf-8'))
        from_client = conn.recv(4096)
        if not from_client: break
        from_client = from_client.decode('utf-8')
        withdraw = int(from_client)
        user_data = user.split(':')
        balance = int(user_data[2])
        if balance >= withdraw:
            balance -= withdraw
            user_data[2] = str(balance)
            user = ''
            for i in user_data:
                user += i + ':'
            user = user[0:len(user)-1]+"\n"
            text[counter] = user
            users = open("Users.txt", "w")
            users.writelines(text)
            users.close()
        conn.send(("balance= "+str(balance)).encode('utf-8'))
        break
    break
conn.close()
print ('client disconnected')
