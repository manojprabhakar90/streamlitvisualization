import streamlit as st
import pandas as pd
import time
import plotly.express as px
import country_converter as coco
import plotly.figure_factory as ff
import plotly.graph_objects as go

st.write("There is always a question on the earning potential on completion of the Data Science degree. Let's start understanding the number of jobs over the past few years")

data = pd.read_csv("ds_salaries.csv")

st.write("We will start exploring the work year. Are the jobs increasing or decreasing")

work_year = data['work_year'].value_counts()
fig = px.pie(values = work_year.values, names = work_year.index, 
            title = 'Work year distribution',color_discrete_sequence=["green", "blue", "goldenrod", "magenta"])
st.plotly_chart(fig)

st.write("Based on the chart, we could see the number of jobs have been increasing in last couple of years, even when there is recession.") 

st.write("Let's look at number of jobs by experience level.") 

data['experience_level'] = data['experience_level'].replace('EN','Entry-level/Junior')
data['experience_level'] = data['experience_level'].replace('MI','Mid-level/Intermediate')
data['experience_level'] = data['experience_level'].replace('SE','Senior-level/Expert')
data['experience_level'] = data['experience_level'].replace('EX','Executive-level/Director')

ex_level = data['experience_level'].value_counts()
fig = px.treemap(ex_level, path = [ex_level.index], values = ex_level.values, 
                title = 'Experience Level',color_discrete_sequence=["green", "blue", "goldenrod", "magenta"])
st.plotly_chart(fig)

st.write("We could see that the number of jobs in Senior-level/Expert have increased when compared to entry level or at Executive level.") 

st.write("Lets look at how the salary has changed over the years" )

data1=data[['work_year','salary_in_usd']].groupby(['work_year']).mean().reset_index()
fig = px.bar(data1, x="work_year", y="salary_in_usd",color_discrete_sequence=["blue"])
st.plotly_chart(fig)

work_2020 = data.loc[(data['work_year'] == 2020)]
work_2021 = data.loc[(data['work_year'] == 2021)]
work_2022 = data.loc[(data['work_year'] == 2022)]
work_2023 = data.loc[(data['work_year'] == 2023)]
 
hist_data = [work_2020['salary_in_usd'], work_2021['salary_in_usd'], 
            work_2022['salary_in_usd'], work_2023['salary_in_usd']]
group_labels = ['2020 salary', '2021 salary', '2022 salary', '2023 salary']

year_salary = pd.DataFrame(columns = ['2020', '2021', '2022', '2023'])
year_salary['2020'] = work_2020.groupby('work_year').mean('salary_in_usd')['salary_in_usd'].values
year_salary['2021'] = work_2021.groupby('work_year').mean('salary_in_usd')['salary_in_usd'].values
year_salary['2022'] = work_2022.groupby('work_year').mean('salary_in_usd')['salary_in_usd'].values
year_salary['2023'] = work_2023.groupby('work_year').mean('salary_in_usd')['salary_in_usd'].values

fig1 = ff.create_distplot(hist_data, group_labels, show_hist = False)
fig2 = go.Figure(data=px.bar(x = year_salary.columns, 
                            y = year_salary.values.tolist()[0],
                            color = year_salary.columns,
                            title = 'Mean Salary by Work Year'))

fig1.update_layout(title = 'Salary Distribution based on Work Year')
st.plotly_chart(fig1)

data1=data[['work_year','experience_level','salary_in_usd']].groupby(['work_year','experience_level']).mean().reset_index()
fig = px.bar(data1, x="work_year", y="salary_in_usd",color="experience_level",barmode="group",color_discrete_sequence=["red", "green", "blue", "goldenrod", "magenta"])
st.plotly_chart(fig)


st.write("As per the chart, the salary has been increasing (which is good for Entry level and Senior Data Scientists). Entry level Data Scientists salary has been increasing from 2020.") 

st.write("Does Remote Jobs provide an opportunity to earn more?")

fig = px.scatter(data, x="work_year", y="salary_in_usd", color="remote_ratio", marginal_y="violin",
           marginal_x="box", trendline="ols", template="simple_white")
st.plotly_chart(fig)

st.write("our hypothesis is correct. Scatter plot has been showing an increasing trend.")_

st.write("Do Employment type have an impact on the salary. Do part-time/contractors get paid more?")

data1=data[['employment_type','salary_in_usd']].groupby(['employment_type']).mean().reset_index()
fig = px.bar(data1, x="employment_type", y="salary_in_usd",color_discrete_sequence=["blue"])
st.plotly_chart(fig)

st.write("Full Time employees are paid more followed by part-time employees.")

st.write("Highest paid job title")

data1=data[['job_title','salary_in_usd']].groupby(['job_title']).mean().reset_index()
data1 = data1.sort_values(by='salary_in_usd',ascending=False)
fig = px.bar(data1, x="job_title", y="salary_in_usd",color_discrete_sequence=["blue"])
st.plotly_chart(fig)

st.write("Data Science Tech lead gets paid the most. But it's a very small sample. So cannot come to conclusive conclusion ")

data1=data[['employee_residence','salary_in_usd']].groupby(['employee_residence']).mean().reset_index()
data1 = data1.sort_values(by='salary_in_usd',ascending=False)
fig = px.bar(data1, x="employee_residence", y="salary_in_usd",color_discrete_sequence=["blue"])
st.plotly_chart(fig)


remote_year = df.groupby(['work_year','remote_ratio']).size()
ratio_2020 = np.round(remote_year[2020].values/remote_year[2020].values.sum(),2)
ratio_2021 = np.round(remote_year[2021].values/remote_year[2021].values.sum(),2)
ratio_2022 = np.round(remote_year[2022].values/remote_year[2022].values.sum(),2)
ratio_2023 = np.round(remote_year[2023].values/remote_year[2023].values.sum(),2)

fig = go.Figure()
categories = ['No Remote Work', 'Partially Remote', 'Fully Remote']
fig.add_trace(go.Scatterpolar(
            r = ratio_2020, theta = categories, 
            fill = 'toself', name = '2020 remote ratio'))

fig.add_trace(go.Scatterpolar(
            r = ratio_2021, theta = categories,
            fill = 'toself', name = '2021 remote ratio'))

fig.add_trace(go.Scatterpolar(
            r = ratio_2022, theta = categories,
            fill = 'toself', name = '2022 remote ratio'))

fig.add_trace(go.Scatterpolar(
            r = ratio_2023, theta = categories,
            fill = 'toself', name = '2023 remote ratio'))

st.plotly_chart(fig)

st.write("2021 had maximum remote work. With companies relaxing WFH, the number of companies providing WFH have significantly reduced.")

st.write("What is happening to 100% Remote work companies. Are their salaries increasing or decreasing. ")

data1=data[data['remote_ratio']==100]

fig = px.scatter(data1, x="work_year", y="salary_in_usd", trendline="ols", template="simple_white")
st.plotly_chart(fig)

st.write("We could see that the salary has been increasing YOY right from 2020 (For all Data Science related roles).")

data1=data[['work_year','company_size','salary_in_usd']].groupby(['work_year','company_size']).mean().reset_index()
fig = px.bar(data1, x="work_year", y="salary_in_usd",color="company_size",barmode="group",color_discrete_sequence=["red", "green", "blue", "goldenrod", "magenta"])
st.plotly_chart(fig)

test=data[['job_title','experience_level']].groupby(['job_title']).count().reset_index().sort_values(by='experience_level',ascending=False)

country = coco.convert(names = data['employee_residence'], to = "ISO3")
data['employee_residence'] = country
country = coco.convert(names = data['employee_residence'], to = "ISO3")
data['employee_residence'] = country
residence = data['employee_residence'].value_counts()
fig = px.choropleth(locations = residence.index,
                    color = residence.values,
                    color_continuous_scale=px.colors.sequential.YlGn,
                    title = 'Employee Loaction On Map')
st.plotly_chart(fig)

st.write("Most of the Employee locations are based out of US as number of employees in US is also high")
work_2020 = data.loc[(data['work_year'] == 2020)]
work_2021 = data.loc[(data['work_year'] == 2021)]
work_2022 = data.loc[(data['work_year'] == 2022)]
work_2023 = data.loc[(data['work_year'] == 2023)]
 
hist_data = [work_2020['salary_in_usd'], work_2021['salary_in_usd'], 
            work_2022['salary_in_usd'], work_2023['salary_in_usd']]
group_labels = ['2020 salary', '2021 salary', '2022 salary', '2023 salary']

year_salary = pd.DataFrame(columns = ['2020', '2021', '2022', '2023'])
year_salary['2020'] = work_2020.groupby('work_year').mean('salary_in_usd')['salary_in_usd'].values
year_salary['2021'] = work_2021.groupby('work_year').mean('salary_in_usd')['salary_in_usd'].values
year_salary['2022'] = work_2022.groupby('work_year').mean('salary_in_usd')['salary_in_usd'].values
year_salary['2023'] = work_2023.groupby('work_year').mean('salary_in_usd')['salary_in_usd'].values

fig1 = ff.create_distplot(hist_data, group_labels, show_hist = False)
fig2 = go.Figure(data=px.bar(x = year_salary.columns, 
                            y = year_salary.values.tolist()[0],
                            color = year_salary.columns,
                            title = 'Mean Salary by Work Year'))

fig1.update_layout(title = 'Salary Distribution based on Work Year')
st.plotly_chart(fig1)

st.write("Salary distribution based on year. ")

country = coco.convert(names = data['company_location'], to = "ISO3")
data['company_location'] = country
exp_location = data.groupby(['experience_level','company_location']).size()

entry_location = exp_location['Entry-level/Junior']
executive_location = exp_location['Executive-level/Director']
mid_location = exp_location['Mid-level/Intermediate']
senior_location = exp_location['Senior-level/Expert']

fig1 = px.choropleth(locations = entry_location.index, color = entry_location.values,
                    title = 'Entry-level/Junior Company Location')

fig2 = px.choropleth(locations = mid_location.index, color = mid_location.values,
                    title = 'Mid-level/Intermediate Company Location')

fig3 = px.choropleth(locations = senior_location.index, color = senior_location.values,
                    title = 'Senior-level/Expert Company Location')

fig4 = px.choropleth(locations = executive_location.index, color = executive_location.values,
                    title = 'Executive-level/Director Company Location')

fig1.add_scattergeo(locations = entry_location.index, text = entry_location.values,  mode = 'text')
fig2.add_scattergeo(locations = mid_location.index, text = mid_location.values,  mode = 'text')
fig3.add_scattergeo(locations = senior_location.index, text = senior_location.values, mode = 'text')
fig4.add_scattergeo(locations = executive_location.index, text = executive_location.values,  mode = 'text')

st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig3)
st.plotly_chart(fig4)

st.write("Location of different Grade employees. ")
