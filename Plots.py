import matplotlib.pyplot as plt
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#WOMAN
pickle_1 = open("WomanStates.pickle","rb")
D1 = pickle.load(pickle_1)

pd.DataFrame(D1.items())
DC1 = pd.DataFrame(D1.items(), columns=['Label', 'Number'])
DC1['Number'] = pd.to_numeric(DC1['Number'])
DC1 = DC1.dropna()

DC1 = DC1.sort_values(by='Number',ascending=False)

sum = 0
for i in DC1['Number']:
    sum = sum + i

#1560124
if sum == 1561083:
    print('true')
else :
    print("False")
print(sum)

for i in DC1['Label']:
    temp = i.split("-")
    k = temp[-1]
    i = k

#if sum ==





#DC1[DC1['Label'] == "Filed Cases By Woman - Delhi" or i == "Filed Cases By Woman - Maharashtra" or i == "Filed Cases By Woman - Uttar Pradesh" or i == "Filed Cases By Woman - West Bengal" or i == "Filed Cases By Woman - Tamil Nadu"]


'''

df.loc[1,ColNameList1]=1

df.loc[2,ColNameList2]=1

for i in range(1,len(DC1['Label']):
    
    temp = i.split("-")
    DC1[i] = temp[-1]

for j in range(0,32):
    for i in DC1['Label']:
        if i == "Filed Cases By Woman - Delhi" or i == "Filed Cases By Woman - Maharashtra" or i == "Filed Cases By Woman - Uttar Pradesh" or i == "Filed Cases By Woman - West Bengal" or i == "Filed Cases By Woman - Tamil Nadu":
            DC1 = DC1.drop(i,axis=0)

'''





#SENIOR CITIZEN
pickle_2 = open("SeniorCitizenStates.pickle","rb")
D2 = pickle.load(pickle_2)


pd.DataFrame(D2.items())
DC2 = pd.DataFrame(D2.items(), columns=['Label', 'Number'])
DC2['Number'] = pd.to_numeric(DC2['Number'])
DC2 = DC2.drop(0)

DC2 = DC2.sort_values(by='Number',ascending=False)

sum = 0
for i in DC2['Number']:
    sum = sum + i
if sum == 478389:
    print("true")
print(sum)

for i in DC2['Label']:
    temp = i.split("-")
    k = temp[-1]
    i = k

'''corr = DC2.corr()
ax = sns.heatmap(
    corr,
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
)

plt.show()'''

'''
for i in DC2['Label']:
    temp = i.split("-")
    i = temp[-1]
    print(i)
    '''

#STAGE WISE
pickle_3 = open("StageWise123.pickle","rb")
D3 = pickle.load(pickle_3)

pd.DataFrame(D3.items())
DC3 = pd.DataFrame(D3.items(), columns=['Label', 'Number'])
DC3['Number'] = pd.to_numeric(DC3['Number'])

DC3 = DC3.sort_values(by='Number',ascending=False)

DC3 = DC3.dropna()


'''for i in DC3['Number']:
    temp = i.split("-")
    k = temp[-1]
    i = k'''

if sum == 478389:
    print("true")
print(sum)



#PENDING CASE WISE
pickle_4 = open("PendingCases.pickle","rb")
D4 = pickle.load(pickle_4)

pd.DataFrame(D4.items())
DC4 = pd.DataFrame(D4.items(), columns=['Label', 'Number'])
#DC4['Number'] = pd.to_numeric(DC4['Number'])

DC4 = DC4.sort_values(by='Number',ascending=False)

DC4 = DC4.dropna()

'''sum = 0
for i in DC2['Number']:
    sum = sum + i
if sum == 478389:
    print("true")
print(sum)'''


#DC1.plot(x="Label", y="Number", kind="bar")



ax = DC1.plot(x="Label", y="Number", kind="bar")
plt.title('Woman')
plt.xlabel('States')
plt.ylabel('Number of Cases')
#plt.show()

ax = DC2.plot(x="Label", y="Number", kind="bar")
plt.title('Senior Citizen')
plt.xlabel('States')
plt.ylabel('Number of Cases')
#plt.show()

ax = DC3.plot(x="Label", y="Number", kind="bar")

#df.plot(x="X", y="B", kind="bar", ax=ax, color="C2")
#df.plot(x="X", y="C", kind="bar", ax=ax, color="C3")



print(D1)
print(DC1)
print(D2)
print(DC2)
print(D3)
print(DC3)
print(DC4)


