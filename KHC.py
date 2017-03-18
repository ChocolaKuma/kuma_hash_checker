import time
import hashlib

pass_check_result = False

time_start = time.time()

pass2check = "37b4e2d82900d5e94b8da524fbeb33c0"
pass3check = "football"

passwordlist = ["password","123456","12345678","1234","qwerty","12345","baseball",
                 "football","letmein","monkey","abc123","mustang","michael"]

E_passwordlist = [
 '5f4dcc3b5aa765d61d8327deb882cf99',
 'e10adc3949ba59abbe56e057f20f883e',
 '25d55ad283aa400af464c76d713c07ad',
 '81dc9bdb52d04dc20036dbd8313ed055',
 'd8578edf8458ce06fbc5bb76a58c5ca4',
 '827ccb0eea8a706c4c34a16891f84e7b',
 '276f8db0b86edaa7fc805516c852c889',
 '37b4e2d82900d5e94b8da524fbeb33c0',
 '0d107d09f5bbe40cade3de5c71e9e9b7',
 'd0763edaa9d9bd2a9516280e9044d885',
 'e99a18c428cb38d5f260853678922e03',
 'bee783ee2974595487357e195ef38ca2',
 '0acf4539a14b3aa27deeb4cbdf6e989f']

def one_hash(key_string):
    key_string = key_string.encode('utf-8')
    e_pass = hashlib.md5(key_string).hexdigest()
    return e_pass


def list_hash(r_passwordlist):
    out = []
    print("")
    for x in r_passwordlist:
        e_passwordlist = one_hash(x)
        out.append(x)
        out.append(e_passwordlist)
    return out


def pass_check(pass_to_be_checked,e_passwordlist):

    pass_check_result = e_passwordlist.index(pass_to_be_checked)
    return pass_check_result



def IO_hash(mode=0):
    if (mode==0):
        print("nothing ran")
        
    if (mode==1):
        r_pass = str(input("Password:\n"))
        e_pass = one_hash(r_pass)
        print(r_pass,",",e_pass)
        
    if (mode==2):
        out = list_hash(passwordlist)
        print(out)
        
    if(mode==3):
        r_pass = pass3check
        e_pass = one_hash(r_pass)
        try:
            result = pass_check(e_pass,E_passwordlist)
            print("Password was in DB\n")
            print("Password "," MD5 Hash")
            print(r_pass,":",e_pass)
            
        except:
            print("password not in DB")

def main():     
    IO_hash(3)

main()