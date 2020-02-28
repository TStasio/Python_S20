"""
Name: Tanya Stasio
IDCE 302 - Lab 5
Python 2.7.16
Due: 02/2/2020
"""

#Create Dictionary for Refugee Camp and Number of Refugees
#Year chosen: 2006

refugee={"Chad - Am Nabak": 16504,"Yemen - Al Kharaz": 9298, "Sudan - Girba": 8996, "Malawi - Dzaleka": 4950, "Thailand - Mae La": 46148}

#There are multiple camps per country so I am adopting the function to return country/camp combination
#Camps only
def country_camp(dicInput):
    for key in dicInput:
        print(dicInput.keys())
        
country_camp(refugee)

#Values only
def country_camp_values(dicInput):
    for value in dicInput:
        print(dicInput.values())
        
country_camp_values(refugee)

def sentence(dicInput):
    for (key,value) in dicInput.items():
        print(key,"has",value,"refugees")
        
sentence(refugee)

