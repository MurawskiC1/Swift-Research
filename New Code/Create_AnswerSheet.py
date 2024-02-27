import pandas as pd

def ans1(shape):
    if "extended emission" in shape:
        return "Extended"
    elif "simple" in shape:
        return "Simple"
    elif "Other" in shape:
        return "Other"
    elif "too noisy" in shape:
        return "Too Noisy"

      
def ans2(j):
    ans = []
    if 'underlying' in j: 
        ans.append("Underlying Emission")
    if 'symmetrical structure' in j:
        ans.append("Symmetrical Structure")
    if "fast-rise and slow-decay shape" in j:
        ans.append("Fast Rise Slow Decay")
    if 'Rapid Varying pulses' in j:
        ans.append("Rapidly Varying")
    if "I don't see" in j:
        ans.append("Don't See Anything")
    if "too noisy" in j:
        ans.append("Too Noisy")        
    return ans

GRBname = []
Q1answer = []
Q2answer = []
file = open("/Users/catermurawski/Desktop/Swift-Research/Golden_Sample/Golden_sample_list_v1.txt")
run = False
for line in file:
    if run == True:
        seg = line.split("|")
        GRBname.append(seg[0].split(" ")[0])
        Q1answer.append(ans1(seg[1]))
        Q2answer.append(ans2(seg[2]))
    run = True
    
data = {"GRB_Name" : GRBname,
        "Question_1": Q1answer,
        "Question_2": Q2answer
        }

df = pd.DataFrame(data)
df.to_csv("/Users/catermurawski/Desktop/Swift-Research/Golden_Sample/AnswerKey.csv", index=False, header=True)
