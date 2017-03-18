import os     #for os control
import shutil #for dir make and destruction
import random
import distutils.dir_util
import pickle
import hashlib
import time

time_start = time.time()

def value_lookup(LookupNum):
    print(raw[LookupNum]," : ", crypt [LookupNum])
    
def one_hash(key_string,Crypt_type="MD5"):
    if(Crypt_type=="MD5"):
        key_string = key_string.encode('utf-8')
        e_pass = hashlib.md5(key_string).hexdigest()
    return e_pass

def write_array(loc,array_out):
    with open(loc, "wb") as fp:   #Pickling "/sys/rawPassword.txt"
        pickle.dump(array_out, fp)
        
def read_array(loc):
    with open(loc, "rb") as fp:   # Unpickling
        b = pickle.load(fp)
        return b

raw = read_array("sys/rawPassword.txt")
crypt = read_array("sys/cryptPassword.txt")

def main():
    
    print(one_hash("google",Crypt_type="MD5"),"\n\n")
    value_lookup(0)
    #write_array("sys/cryptPassword.txt",E_passwordlist)    




main()
write_array("sys/rawPassword.txt",raw)
write_array("sys/cryptPassword.txt",crypt)
print("\n\n\n\nTime to Complete:",time.time()-time_start,"Secs")
