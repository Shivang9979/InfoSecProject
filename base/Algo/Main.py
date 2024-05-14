import os
from .dataProcessing import *
from .Threads import *

def EncryptInput(data):
	Segment(data)
	gatherInfo()
	HybridCrypt()

def DecryptMessage(data):
    HybridDeCrypt(data)
    trim()
    Merge()
        

# def main(data):
#     EncryptInput(data)
    # DecryptMessage()
    
# if __name__=="__main__":
#     main(data)

