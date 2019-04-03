import configparser

def readconfig(file):
    config = configparser.ConfigParser()
    try:
        if config.read(file) == []:
            raise Exception
    except:
        return None
    
    classroom = []
    for cl in config.sections():
        conf = {'only': '', 'exclude': ''}
        
        if 'only' in config[cl]:
            conf['only'] = config[cl]['only'].split(' ')
        
        if 'Exclude' in config[cl]:
            conf['Exclude'] = config[cl]['Exclude'].split(' ')
        
        classroom.append({cl: conf})
    return classroom
    
#print(readconfig('config.ini'))