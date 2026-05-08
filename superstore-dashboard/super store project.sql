select count( *) from superstore;
select * from superstore
limit 5;

select "superstore.order_Id"
from superstore;

select column_name
fro
select "Profit", count("Product_Name"), "Category","Sub_Category"
from superstore
group by "Product_N", "Category","Sub_Category"
having  "Profit" <0;


select "State",
Sum("Sales") As total_sales
from superstore
group by "State"
order by total_sales Desc
limit 10;


select "Country",
Sum ("Sales") As total_sales
from superstore
group by "Country"
order by total_sales DESC
limit 10;

select "State",
Sum ("Profit") As total_profit
from superstore
group by "State"
order by total_profit DESC
limit 10;

select "Segment",
Sum ("Sales") As total_sales,
Sum ("Profit") As total_profit
from superstore
group by "Segment"
order by total_profit Desc;


select "State",
sum("Profit") As total_profit
from superstore
group by "State"
having   sum("Profit")<0
order by total_profit


SELECT 
    SUM("Sales") AS total_sales,
    SUM("Profit") AS total_profit,
    COUNT("Order_Id") AS total_orders
FROM superstore;


SELECT "Region",
    SUM("Sales") AS total_sales
FROM superstore
GROUP BY "Region"
ORDER BY total_sales DESC;


SELECT "Category",
    SUM("Sales") AS total_sales
FROM superstore
GROUP BY "Category"
ORDER BY total_sales DESC;


SELECT "Sub_Category",
    SUM("Profit") AS total_profit
FROM superstore
GROUP BY "Sub_Category"
ORDER BY total_profit DESC;


SELECT 
    TO_CHAR("Order_Date", 'Month') AS month,
    EXTRACT(MONTH FROM "Order_Date") AS month_num,
    SUM("Sales") AS total_sales
FROM superstore
GROUP BY month, month_num
ORDER BY month_num;


SELECT "Product_Name",
    SUM("Sales") AS total_sales
FROM superstore
GROUP BY "Product_Name"
ORDER BY total_sales DESC
LIMIT 10;





























