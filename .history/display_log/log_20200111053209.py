import subprocess, sys


'''
cmd_log :

    print the loggins obtain from a bash command
    pass the 'commande' at the init instance 

    exemple :

    cmd_log('ls')

'''
class cmd_log():

    def __init__(self,cmd,log_path= ""):
        
        self.cmd = cmd
        self.file = log_path+'log.txt'
        self.log_file_pointer = open(self.file, 'wt')
        self.print_log( files=[self.log_file_pointer, sys.stdout])
    #get bash loggin and convert it in string    
    def get_stdout(self):
        p = subprocess.Popen(self.cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()

        return stdout.decode().replace('\r', '')
    #print  the files content 
    def print_log(self, files=[]):
        get = self.get_stdout()
        for fi in files:
            print(get, file=fi)