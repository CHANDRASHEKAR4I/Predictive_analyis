import streamlit as st
import pickle

# importing model - loan predictive analyser
model = pickle.load(open( ".model\ml_predmodel.pkl",'rb'))
# HERE WE NEED 11 FEATURES TO GIVE INPUT OUR MODEL
#Gender	Married	Dependents	Education	Self_Employed	ApplicantIncome	CoapplicantIncome	LoanAmount	Loan_Amount_Term	Credit_History	Property_Area

# I want to bring our observations here 

Account_id  = st.text_input(" ACCOUNT ID")
#Gender
# yes/no
Gender   = st.radio('SELECT GENDER', ['MALE','FEMALE'])
if Gender=='MALE':
    Gender = 0
else:
    Gender = 1
st.write(Gender)



#Married
# yes/no
Married   = st.radio('married_status', ['No','yes'])
if Married=='No':
    Married = 0
else:
    Married = 1
st.write(Married)
#Dependents
#yes /no
Dependents   = st.radio('No of dependents', ['none', 'one','two', 'morethan3'])
if Dependents=='none':
    Dependents = 0
elif Dependents=='one':
    Dependents = 1
elif Dependents=='two':
    Dependents = 2
else:
    Dependents = 3
st.write(Dependents)

#Education
# graduate/ not graduate
Education   = st.radio('education', ['Graduate','Not Graduate'])
if Education=='Graduate':
    Education = 0
else:
    Education = 1
st.write(Education)

#Self_Employed
# yes / no
Self_Employed   = st.radio('Are you employed', ['No','yes'])
if Self_Employed=='No':
    Self_Employed = 0
else:
    Self_Employed = 1
st.write(Self_Employed)

#ApplicantIncome
# max income - 81000.000000
# min        - 150.000000	

ApplicantIncome = st.slider('your income should be ', min_value=150, max_value=90000)

#CoapplicantIncome
# maxincome - 41667.000000
#min        - 0

CoapplicantIncome = st.slider('coapplicant', min_value=0, max_value=500000)
if Married ==False:
    CoapplicantIncome = 0

st.write(ApplicantIncome)
st.write(CoapplicantIncome)
#LoanAmount
LoanAmount= st.number_input('Enter a reuired amount of loan')


#Loan_Amount_Term
Loan_Amount_Term = st.slider('Loan_Amount_Term', min_value=10, max_value=500)

#Credit_History
Credit_History   = st.radio('credit_history', ['No','yes'])
if Credit_History=='No':
    Credit_History = 0.0
else:
    Credit_History = 1.0
st.write(Credit_History)
#Property_Area

Property_Area   = st.radio('property', ['Urban','rural', 'semiurban'])
if Property_Area=='Urban':
    Property_Area = 0
elif Property_Area=='rural':
    Property_Area = 1
else:
    Property_Area = 2
st.write(Property_Area)


# numeric_list = [Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]
numeric_list = [1,	0,	2,	0,	1,	4583,	0.0,	123.0,	300.0,	1.0,	1	]
prediction=model.predict([numeric_list])


if prediction==False:st.error(f"sorry! your {Account_id} is not elegible for loan")
else: st.success(f"congrats! your {Account_id} is elegible for loan")