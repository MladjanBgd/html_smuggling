import base64

file_path = "C:\dev\html_smuggling\calc.exe"

with open(file_path, 'rb') as f:
    data = f.read()

data_enc = base64.b64encode(data)

#print(data_enc)

file_enc = 'C:\dev\html_smuggling\calc_enc.txt'

with open(file_enc, 'wb') as f:
    f.write(data_enc)

print('completed!')