import pandas as pd

train_df = pd.read_csv("/home/drugdesign/work/BA_CM/new_cma/input/DTA/training.tsv", sep = "\t")
train, train_chains = train_df.iloc[:,0].values, train_df.iloc[:,2].values
print(train_chains)

holo4k_df = pd.read_csv("/home/drugdesign/work/BA_CM/new_cma/input/BS/holo4k.tsv", sep = "\t")
holo4k_chains = holo4k_df.iloc[:,1].values
print(holo4k_chains)

set1_df = pd.read_csv("/home/drugdesign/work/BA_CM/new_cma/input/DTA/CSAR_NRC_HiQ_set1.tsv", sep = "\t")
set1_chains = set1_df.iloc[:,2].values
print(set1_chains)

set2_df = pd.read_csv("/home/drugdesign/work/BA_CM/new_cma/input/DTA/CSAR_NRC_HiQ_set2.tsv", sep = "\t")
set2_chains = set2_df.iloc[:,2].values
print(set2_chains)

total_chains = set()

for i in train_chains:
    t = i.split(",")
    total_chains.add(len(t))
    #for k in t:
    #    total_chains.add(k)

for i in holo4k_chains:
    t = i.split(",")
    total_chains.add(len(t))
    #for k in t:
    #    total_chains.add(k)
        
for i in set1_chains:
    t = i.split(",")
    total_chains.add(len(t))
    #for k in t:
    #    total_chains.add(k)

for i in set2_chains:
    t = i.split(",")
    total_chains.add(len(t))
    #for k in t:
    #    total_chains.add(k)        
      
print(total_chains)
print(len(total_chains))