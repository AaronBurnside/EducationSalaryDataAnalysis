import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

#from sklearn.model_selection import train_test_split  //TODO add Machine Learning predictive model

#This is the Data set containing data on graduates Salaries based on colleges
DataSet_1 = pd.read_csv('salary_data_set_1.csv')
#print(DataSet_1.head())
#print(DataSet_1.describe())
#print(DataSet_1["state_name"].count())
print("The Standard Deviation of early_career_pay is:" + str(DataSet_1["early_career_pay"].std()))
print("The Range of early_career_pay is: " + str((DataSet_1["early_career_pay"].max() - DataSet_1["early_career_pay"].min())))

#here i am finding the overall mean and median of college graduates
College_Mean = DataSet_1["early_career_pay"].mean()
College_Median = DataSet_1["early_career_pay"].median()
print("The Average starting salary of College Grauated across the US: " + str(College_Median))
# it is about $50000.0


#Here i am Gathering the Data based on state the college is in
Average_By_State = DataSet_1[[ "early_career_pay","state_name"]].groupby("state_name").mean().reset_index()


"""column_headers = list(Average_By_State.columns.values)
print(column_headers) """

#print(Average_By_State.head())
#print(Average_By_State)

#Here i am creating a plot that shows the average salary of colloge graduates by state
Average_By_State.plot.bar(x="state_name", y="early_career_pay", alpha=0.5)
plt.show()
Collage_State_Chart = plt.figure()
Collage_State_Chart.savefig("Collage_State_Chart.png")
#the figure shows that graduates from universities in californa, and new york have the best starting salaries


#This is the Data set containing data on Under Grads Salaries based on Degree
DataSet_2 = pd.read_csv('salary_data_set_2.csv')
Undergrad_Mean = DataSet_2["Starting Median Salary"].mean()
Undergrad_Median = DataSet_2["Starting Median Salary"].median()
print("Average Undergrautes median Salary: " + str(Undergrad_Median))
print("The Standard Deviation of Starting Median Salary is:" + str(DataSet_2["Starting Median Salary"].std()))
print("The Range of Starting Median Salary is: " + str((DataSet_2["Starting Median Salary"].max() - DataSet_2["Starting Median Salary"].min())))



#Here i am creating a plot that shows the average salary of colloge graduates by undergaduate Major
DataSet_2.plot.bar(x="Undergraduate Degree", y="Starting Median Salary", alpha=0.5)
plt.show()
Collage_Major_Chart = plt.figure()
Collage_Major_Chart.savefig("Collage_Major_Chart.png")
#this figure showed that Physician Assistant had by fare the highest salary, followed by the various engineering majors


#This is the Data set containing data on Graduates Salaries based on Major catogory / department/ field
DataSet_3 = pd.read_csv('salary_data_set_3.csv')
print(DataSet_3["Major_category"].count())
Average_By_Catagory = DataSet_3[["Major_category", "Median"]].groupby("Major_category").mean().reset_index()
print("The Standard Deviation of Median Salary by field is:" + str(Average_By_Catagory["Median"].std()))
print("The Range of Median Salary by Field is: " + str((Average_By_Catagory["Median"].max() - Average_By_Catagory["Median"].min())))






#Here i am creating a plot that shows the average salary of Under graduates by Major catogory/department/field
Average_By_Catagory.plot.bar(x="Major_category", y="Median", alpha=0.5)
plt.show()
Average_By_Catagory_Chart = plt.figure()
Average_By_Catagory_Chart.savefig("Average_By_Catagory.png")
#this figure showed that the engineering department graduates had the highest median pay, surpassing the health department


#This is the Data set containing data on the Salaries of those who have and have not graduated highschool based on state 
DataSet_4 = pd.read_csv('salary_data_set_4.csv')

Non_grad_Mean = DataSet_4["Non-grad"].mean()
Non_grad_Median = DataSet_4["Non-grad"].median()

High_School_grad_Mean = DataSet_4["High-School-Grad"].mean()
High_School_grad_Median = DataSet_4["High-School-Grad"].median()


#Here i am creating a plot that shows the average salary of those who did not graduate high school sorted by state
DataSet_4.plot.bar(x="state_name", y="Non-grad", alpha=0.5)
plt.show()
Non_grad_Chart = plt.figure()
Non_grad_Chart.savefig("Non_grad_Chart.png")
#this figure showed that North Dakota had the highest average Non-Gradaute Salary


#Here i am creating a plot that shows the average salary of those whose highest education is a high school diploma sorted by stata
DataSet_4.plot.bar(x="state_name", y="High-School-Grad", alpha=0.5)
plt.show()
High_School_grad_Chart = plt.figure()
High_School_grad_Chart.savefig("Non_grad_Chart.png")
#this figure showed that Massachusetts had the highest average High School Graduate Salary 


State_Comparison = pd.merge(DataSet_4, Average_By_State, how="left", on="state_name")
#print(State_Comparison)


New_data = State_Comparison.reset_index().melt('state_name')
""" State_Comparison_Chart = alt.Chart(New_data).mark_line().encode(
    x='state_name',
    y='value',
    color='variable'
)
 """

C_H_Change = College_Median / High_School_grad_Median
H_N_Change = High_School_grad_Median / Non_grad_Median
print("Average High school Drop out median Salary: " + str(Non_grad_Median))
print("Average High school Graduates median Salary: " + str(High_School_grad_Median) + "Which is " + str(H_N_Change) + " Times higher than Dropouts")
print("Average College Graduates median Salary: " + str(College_Median) + "Which is " + str(C_H_Change) + " Times higher than High School Graduates")

#High School Graduates earn 23.5% more than Drop outs on average
#College Graduates hearn around 55% more than High school Graduates on Average



