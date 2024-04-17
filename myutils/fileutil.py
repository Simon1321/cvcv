def print_file_info(file_name):
    f= None
    try:
        f=open(file_name,'r',encoding = 'UTF-8')
    except Exception as e :
        print(e)
    else :
        lines = f.readlines()
        for line in lines:
            print(line,end = '')
    finally:
        f.close()

def append_to_file(file_name,data):
    f=open(file_name,'a+',encoding = 'UTF-8')
    f.write(data)
    lines = f.readlines()
    for line in lines:
        print(line, end='')
    f.close()
