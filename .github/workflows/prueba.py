import mysql.connector
import sys
import git
import os
import yaml

 

#path=sys.argv[1]
#print ("path:  "+path)

 
path="/Users/andresjimenez/Documents/GitHub/pruebas_actions"
repo = git.Repo("/Users/andresjimenez/Documents/GitHub/pruebas_actions")
hcommit = repo.head.commit

for diff_added in hcommit.diff("HEAD~1"):
    fileChanged=str(diff_added).split("==")[0].rstrip()
    ruta = path+"/"+fileChanged
    print("fichero->  "+path+"/"+fileChanged)
 
    with open(ruta, 'r') as file:
        field_list = yaml.safe_load(file)

 

        print(field_list)