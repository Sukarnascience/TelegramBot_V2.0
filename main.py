import aiml

if(__name__=="__main__"):
    kernel = aiml.Kernel()
    kernel.learn("std-startup.xml")
    kernel.respond("LOAD AIML B")