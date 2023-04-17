import hashlib
import endc
import contractBlock as md

def checkImage(image):
    res = str(hashlib.md5((image).tobytes()).hexdigest())
    message = md.contract.functions.sayHello(res).call()
    message = str(message)+str('\n')+ str('Text Encoded in Image : ') +str(endc.decode(image=image))
    
def generateImage(image,text):
    endc.encode(image,text)
    
