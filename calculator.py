import streamlit as st
import math

st.markdown("<h1 style='text-align: center;'>Education Loan Calculator</h1>", unsafe_allow_html=True)


column1,column2 =st.columns(2, gap="large" )
with column1:
    st.write("### input Data")

    loan_amount = st.number_input("Loan amount", min_value=0 )
    Intrest_rate= st.number_input("Interest rate (in %)", min_value= 0.0 , value=9.5  )
    loan_tenure = st.number_input("loan tenure (in years)", min_value=1 )

monthly_intrest_rate = (Intrest_rate/100) /12
number_of_payments =loan_tenure *12
blah_blah = (1+ monthly_intrest_rate) ** number_of_payments

EMI = ((loan_amount * monthly_intrest_rate * blah_blah)/(blah_blah -1))
total_payment= (EMI * number_of_payments)
total_interest = math.trunc((EMI*number_of_payments)-loan_amount)

with column2:
    st.write("### Repayments")
    st.metric(label="# Monthly Repayment (EMI)", value=f"{EMI:,.0f}")
    st.metric(label="Total repayment", value=f"{total_payment:,.0f} ")
    st.metric(label="Total interest", value=f"{total_interest:,.0f}")


# Pie chart
import streamlit as st
import plotly.express as px

labels = ['Loan Amount', 'Total Interest', 'Total Payable Amount']
sizes = [loan_amount, total_interest, total_payment] 
st.markdown("<h3 style='text-align: center;'>break-down of total payment</h3>", unsafe_allow_html=True)

fig = px.pie(values=sizes, names=labels,
             hover_data={'values': sizes}, labels={'values':'Quantity'})

fig.update_traces(textinfo='label+value')

st.plotly_chart(fig)
