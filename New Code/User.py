import pandas as pd
        


class User:
    def __init__(self, name):
        self.name = name
        
        self.classifications = 0
        self.score = None
        self._correct = 0
        self._incorrect = 0
        self._pcorrect = 0
        self._pincorrect = 0
        self.accuracy = None
        self.paccuracy = None
        self.pscore = None
        
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, i):
        self._name = i
        
    @property
    def accuracy(self):
        return self._accuracy
    
    @accuracy.setter
    def accuracy (self, i):
        self._accuracy = i
    @property
    def paccuracy(self):
        return self._paccuracy
    
    @paccuracy.setter
    def paccuracy (self, i):
        self._paccuracy = i
        
    @property
    def classifications(self):
        return self._classifications
    
    @classifications.setter
    def classifications(self, i):
        self._classifications = i
        
        
    @property
    def ans(self):
        return self._ans
    
    @ans.setter
    def ans(self, i):
        self._ans = i
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score (self, i):
        self._score = i
        
    @property
    def pscore(self):
        return self._pscore
    
    @pscore.setter
    def pscore (self, i):
        self._pscore = i
        
    @property
    def classifications(self):
        return self._classifications
    
    @classifications.setter
    def classifications(self, i):
        self._classifications = i
    
    def classify(self):
        self.classifications += 1
        
    def grade(self, key, results):
        if key[0].upper() in results.upper():
            self._correct +=1
        else:
            self._incorrect +=1
        self.accuracy = f"{(self._correct)}/{(self._correct+self._incorrect)}"
        self.score = (self._correct)/(self._correct+self._incorrect)
    def gradep(self, key, results):
        if key[0].upper() in results.upper():
            self._pcorrect +=1
        else:
            self._pincorrect +=1
        self.paccuracy = f"{(self._pcorrect)}/{(self._pcorrect+self._pincorrect)}"
        self.pscore = (self._pcorrect)/(self._pcorrect+self._pincorrect)
        
def findName(n):
    try:
        n = n.split("batgrbcat//")
        n = n[1].split("/web/GRB")
        return n[0]
    except:
        return "No Name Found"
    
key = {}
ans = open("/Users/catermurawski/Desktop/Swift-Research/Golden_Sample/AnswerKey.csv")
beta = pd.read_csv("/Users/catermurawski/Desktop/burst-chaser-classifications.csv")
for i in ans:
    j = i.split(",")
    key[j[0]]= j[1:2]
    
users = {}
for i in range(11101,beta.shape[0]):
    workflow = beta.workflow_name.iloc[i]
    wid = beta.workflow_id.iloc[i]
    id_number = beta.subject_ids.iloc[i]
    results = beta.annotations.iloc[i]
    user = beta.user_name.iloc[i]
    burst_name = findName(beta.subject_data.iloc[i])
    
    if user not in users:
        users[user] = User(user)
    users[user].classify()
    if workflow == "Pulse shapes":
        if burst_name in key:
            users[user].grade(key[burst_name], results)
    if workflow == "(Optional) Practice: Pulse Shapes":
        if burst_name in key:
            print("hello2")
            users[user].gradep(key[burst_name], results)
    

    
data = {"User": [i for i in users],
        "Classifications": [users[i].classifications for i in users],
        "Accuracy": [users[i].accuracy for i in users],
        "Score": [users[i].score for i in users],
        "Practice_Accuracy": [users[i].paccuracy for i in users],
        "Practice_Score": [users[i].pscore for i in users],
        }
                            
df = pd.DataFrame(data)

df.to_csv("/Users/catermurawski/Desktop/Swift-Research/CSVExports/UserReport.csv", index=False, header=True)
        
        
            
      
    