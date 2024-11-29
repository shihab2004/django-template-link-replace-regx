import re



path = input("File Path: ")
first_expression = input("Fist expression: ")
print("[1] single quotation   [2] double quotation")
quotation = int(input('=> '))
if quotation == 1:
    quotation = "'"
    _quotation = '"'
elif quotation == 2:
    quotation = '"'
    _quotation = "'"
else:
    print("Failed....")
    exit()

def format_replace(format):
    with open(path,"r+") as  f:
        text = f.read()
        a = re.findall(f'{quotation}{first_expression}.*\.{format}{quotation}',text)
        
        _i = []
        for i in a:
            
            
            if i in _i:
                continue
            
            s_text = f"""{_quotation}{{% static {i} %}}{_quotation}"""
            
            print(i)
            print("=>",s_text)
            text = text.replace(i, s_text)
            _i.append(i)
        
        f.seek(0)
        f.write(text)
    

    
formats = ['png','svg','css','js','jpg','ico']

for i in formats:
    format_replace(i)
    
print("Done")
input()