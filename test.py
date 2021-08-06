# -*- coding: utf-8 -*-
import hashlib
from colorama import Back,Style,Fore,init
import time
import codecs
from itertools import (takewhile,repeat)
from pprint import pprint

init(autoreset=True)

def lineCounter(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    print("lines :"+str(i + 1))
    return i + 1

def hash256(wordlistpassword):
    result = hashlib.sha256(wordlistpassword.encode())
    return result.hexdigest()

def read_in_chunks(file_object, chunk_size=10):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        datas = file_object.read(chunk_size)
        b = datas.split()
        if not datas:
            break
        for data in b:
            yield hash256(data), data

    
def bruteforce(actual_password_hash):
        print("Guessing ... ")
        c=0
        starter = time.time()

        with codecs.open(filename, 'r', encoding='latin-1', errors='ignore') as f:
            for guess_password, word_try in read_in_chunks(f):
                # KEY SPEED CALC
                c+=1
                if time.time()-starter >= float(1.00):
                    try:
                        print(str(c) + " Keys/s")
                        starter = time.time()
                        c=0
                    except:pass
                # END KEY SPEED CALC
                # print(str(c) + ":" + guess_password + "  VS  " + actual_password_hash)
                if guess_password == actual_password_hash:
                    f.close()
                    print(Fore.GREEN + "Hey! your password is : " + word_try + " on the try :" + str(c))
                    # If the password is found then it will terminate the script here
                    print(Fore.YELLOW + "Time Taken: "+str(time.time() - start_time))
                    exit()
        f.close()
        print("lines dones : ",c)
        print("Time Taken",time.strftime('%H:%M:%S', time.gmtime(time.time() - start_time)))
        print(Fore.RED+"No Password Found")
        
def rawincount(filename):
    f = open(filename, 'rb')
    bufgen = takewhile(lambda x: x, (f.raw.read(1024*1024) for _ in repeat(None)))
    return sum( buf.count(b'\n') for buf in bufgen )
    
start_time = time.time()
filename = "rockyou.txt"
# lineCounter(filename)
actual_password = 'abygurl69'
actual_password_hash = hash256(actual_password)
print("Initial hash pass : " + actual_password_hash)
total_rows = int(rawincount(filename))
parsed = int(1024/total_rows)
bruteforce(actual_password_hash)
print(parsed)
