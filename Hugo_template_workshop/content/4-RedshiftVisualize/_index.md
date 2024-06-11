---
title : "Running Data Pipeline and Visualization Redshift Data"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 4. </b> "
---
* In this section,we will run all the steps of our data pipeline to gain an overview of the project.Then, we will use **Redshift chart** to get basic insights into the **Customer Data**  stored in our **Redshift Data Warehouse**

## Run all the steps of Data Pipeline.
1. Run Data Generator
![image](/images/Lambda/1.png)
2. Data is stored in **S3 data lake**.
![image](/images/Lambda/2.png)
![image](/images/Lambda/3.png)
3. Data is stored in **Redshift datawarehouse**.
![image](/images/Lambda/4.png)
## Redshift Chart
1. Distribution of Customers by Gender 
```sql
select gender, count(*) as amount
from customers
group by gender;
```
![image](/images/Redshift_Visualize/1.png)
2. Top 10 Products by Sales
```sql
select product_name, count(*)
from products
group by product_name
order by count(*) desc
limit 10;
```
![image](/images/Redshift_Visualize/2.png)
3. Number of Sales Over Time 
```sql
select purchase_date, amount
from transactions
order by purchase_date;
```
![image](/images/Redshift_Visualize/3.png)
4. Age distribution of Customers
```sql
select age, count(*)
from customers
group by age
order by age;
```
![image](/images/Redshift_Visualize/4.png)