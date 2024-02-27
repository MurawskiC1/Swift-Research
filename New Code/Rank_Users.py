import pandas as pd
golden = open("/Users/catermurawski/Desktop/Swift-Research/Golden_Sample/Golden_sample_list_v1.txt")
header = False
name = []
answer = []
def read(n):
    if "imple" in n:
        return "Simple"
    if "ext" in n:
        return "Extended"
    if "ther" in n:
        return "Other"
    
for i in golden:
    if header == True:
        line = i.split("|")
        name.append(line[0])
        answer.append(read(line[1]))
    header = True
    
data = {"Name" : name,
        "Answer" : answer}

df = pd.DataFrame(data)

df.to_csv("/Users/catermurawski/Desktop/Swift-Research/Golden_Sample/G_Sample.csv", index=False,  header= True)
    