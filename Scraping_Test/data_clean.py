import ast
data = input()
data = ast.literal_eval(data)
final = {}
id = 1
for i in data.keys():
    final[i] = {}
    for j in data[i].keys():
        if j=='Name':
            continue
        elif data[i][j]['docs']=={}:
            continue
        else:
            final[i][j] = data[i][j]['docs']
            final[i][j]["ID"] = id
            id+=1
print(final)