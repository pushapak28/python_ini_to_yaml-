from configparser import ConfigParser
import yaml
  
configur = ConfigParser()
configur.read("abc.ini")

datacamp = {}
for section in configur.sections():
    datacamp[section] = {}
    for name,value in configur.items(section):
        xy = datacamp[section].update({name:value})
        

with open("xyz.yaml","w") as ymlfile:
    yaml.dump(datacamp,ymlfile,default_flow_style=False)   


