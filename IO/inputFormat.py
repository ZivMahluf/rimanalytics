def format(arr):
    file = []
    string = ''
    for line in arr:
        string = ''
        for l in line:
            if(l == ''):
                string += 'EMPTY|'
            elif(l == None):
                pass
            else:
                string += l + '|'
        file.append(string[:-1]+'\n')
    saveFile('table',file[:-1])
    return file[:-1]


def saveFile(name,arr):
    f = open("session_DB/"+name + ".txt", "w+")
    for line in arr:
        f.write(line)
    f.close()

