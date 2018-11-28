import os 

print("Running clustering script with mail data")
PARENT_DIR = os.path.dirname((os.path.abspath(__file__)))
os.system('python '+ PARENT_DIR + '/Pred/PrepareData.py')