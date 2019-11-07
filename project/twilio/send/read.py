import json
dir=r"C:\zhujibao\Domains\wangxiaoming.com.cn\public_html\send"
def savejson():
    with open(dir+r"\newfile.json",'r') as load_f:
        newthing = json.load(load_f)
        #newthing=json.loads(load_dict)
        #print(load_dict)
        #print(len(load_dict))
    
    oldfile=open(dir+r"\oldfile.txt","a")
    oldfile.write("account_sid  "+newthing["account_sid"]+"  auth_token  "+
                  newthing["auth_token"]+"  city  "+newthing["city"]+
                  "  tophone  "+newthing["tophone"]+"  fromphone  "+newthing["fromphone"]+"\n")
    '''
    with open(dir+r"\oldfile.json",'r') as load_f2:
        load_dict2 = json.load(load_f2)
        oldthing=json.loads(load_dict2)
        #print(load_dict2)

    print(newthing["account_sid"])
    oldthing.append(newthing)
        #print(load_dict)

    with open(dir+r"\oldfile.json","w") as f:
        json.dump(load_dict,f)
        #print("OK...")
     '''   
savejson()
