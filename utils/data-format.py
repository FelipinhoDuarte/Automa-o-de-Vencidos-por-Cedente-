
# list(map(lambda x:x, data[3])

def data_format():
    from datetime import datetime
    data = datetime.now().strftime("%Y-%m-%dT%H:%M:%S-03:00").split('-')
    ano = data[0]
    mes = data[1]
    dia = data[2].split('T')[0]
    return f'{dia}/{mes}/{ano}'
    
print(data_format())

