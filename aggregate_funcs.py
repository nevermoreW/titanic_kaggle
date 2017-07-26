import pandas as pd
pd.options.mode.chained_assignment = None


def load_titanic_data():
    return pd.read_csv('train.csv')

def aggregate_one(titanic_data):
    titanic_data_copy=titanic_data.dropna(subset=['Age', 'Embarked', 'Sex'])
    age=[]
    embark_id=[]
    sex_id=[]
    age_titanic_data=titanic_data_copy["Age"].values
    embark_titanic_data=titanic_data_copy["Embarked"].values
    sex_titanic_data=titanic_data_copy["Sex"].values

    for sex in sex_titanic_data:
        if sex=='male':
            sex_id.append(1)
        elif sex=='female':
            sex_id.append(2)
        
    for embark in embark_titanic_data:
        if embark=='C':
            embark_id.append(1)
        elif embark=='Q':
            embark_id.append(2)
        elif embark=='S':
            embark_id.append(3)
        
    for age_of_pass in age_titanic_data:
        if age_of_pass<=14:
            age.append(1)
        elif age_of_pass>14 and age_of_pass<=24:
            age.append(2)
        elif age_of_pass>24 and age_of_pass<=64:
            age.append(3)
        elif age_of_pass>64:
            age.append(4)
        else:
            print age_of_pass
    titanic_data_copy["New_Age"]=age
    titanic_data_copy["New_Embarked"]=embark_id
    titanic_data_copy["New_Sex"]=sex_id
    return titanic_data_copy[["New_Age", "Pclass", "Survived", "SibSp", "Parch", "New_Embarked", "New_Sex"]]
            

def getFeatures(listOfFeatures, titanic_data):
    temp_df=pd.DataFrame([])
    for feature in listOfFeatures:
        temp_df["%s"%feature]=titanic_data["%s"%feature]
    return temp_df

#TODO: Change hard-coding of ['C', 'Q', 'S']
def embark(titanic_data):
    returner=getFeatures(["Survived", "Embarked"], titanic_data)

    total_from_each_dest=map(lambda a: len(filter(lambda x: x is a, returner["Embarked"].values)), ['C', 'Q', 'S'])

    returner=returner.query('Survived==1')

    total_surv_from_each_dest=map(lambda a: len(filter(lambda x: x is a, returner["Embarked"].values)), ['C', 'Q', 'S'])
    surv_perc=map(lambda x,y: x/float(y), total_surv_from_each_dest, total_from_each_dest)
    print len(surv_perc)
    return pd.DataFrame([surv_perc], columns=['C%','Q%','S%'])


##
# Load titanic data
"""
titanic_data=load_titanic_data()
print titanic_data.Fare.describe()
print titanic_data["Cabin"].iloc[0:100]

##
# Drop rows for NA values in Age column.
titanic_data=aggregate_one(titanic_data)
titanic_data_matrix=titanic_data.as_matrix()
"""





















