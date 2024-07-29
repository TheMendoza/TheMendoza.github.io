## SQL

## Pizza Data Analysis

### 1. What are the top 3 busiest days, when the most orders are received?
```javascript
SELECT o.date, COUNT(DISTINCT o.order_id) AS total_orders
FROM orders o
JOIN order_details od ON o.order_id = od.order_id
GROUP BY o.date
ORDER BY total_orders DESC
LIMIT 3;
```
- 2015/11/27 115
- 2015/11/26 113
- 2015/10/15 107

### 2. What time of day are most orders placed?
```javascript
SELECT HOUR(time) AS order_hour, COUNT(*) AS total_orders
FROM orders
GROUP BY HOUR(time)
ORDER BY total_orders DESC
LIMIT 1;
```
- Order hour 12
- Total orders 3829

### 3. Percentage of Sales by Pizza Category
```javascript
SELECT 
    pt.category,
    SUM(od.quantity * p.price) AS category_sales,
    (SUM(od.quantity * p.price) / total_sales.total_revenue) * 100 AS sales_percentage
FROM 
    orders o
JOIN 
    order_details od ON o.order_id = od.order_id
JOIN 
    pizzas p ON od.pizza_id = p.pizza_id
JOIN 
    pizza_types pt ON p.pizza_type_id = pt.pizza_type_id,
    (SELECT SUM(od.quantity * p.price) AS total_revenue
     FROM orders o
     JOIN order_details od ON o.order_id = od.order_id
     JOIN pizzas p ON od.pizza_id = p.pizza_id) total_sales
GROUP BY 
    pt.category, total_sales.total_revenue
ORDER BY 
    sales_percentage DESC;
```
- Classic 331348 sales equals 26.8%
- Supreme 315138 sales equals 25.5%
- Chicken 295214 sales equals 23.9%
- Veggie 293174 sales equals 23.7%

### 4. Percentage of Sales by Pizza Size
```javascript
SELECT 
    p.size,
    SUM(od.quantity * p.price) AS size_sales,
    (SUM(od.quantity * p.price) / total_sales.total_revenue) * 100 AS sales_percentage
FROM 
    orders o
JOIN 
    order_details od ON o.order_id = od.order_id
JOIN 
    pizzas p ON od.pizza_id = p.pizza_id,
    (SELECT SUM(od.quantity * p.price) AS total_revenue
     FROM orders o
     JOIN order_details od ON o.order_id = od.order_id
     JOIN pizzas p ON od.pizza_id = p.pizza_id) total_sales
GROUP BY 
    p.size, total_sales.total_revenue
ORDER BY 
    sales_percentage DESC;
```
- size	size_sales	sales_percentage
- L	    567131.2	45.92616029
- M	    376487.75	30.48789549
- S	    267938.95	21.69763745
- XL	21700.5	    1.757301734
- XXL	1617.75	    0.13100504

### 5. Total Pizzas Sold by Pizza Category
```javascript
SELECT 
    pt.category,
    SUM(od.quantity) AS total_pizzas_sold
FROM 
    orders o
JOIN 
    order_details od ON o.order_id = od.order_id
JOIN 
    pizzas p ON od.pizza_id = p.pizza_id
JOIN 
    pizza_types pt ON p.pizza_type_id = pt.pizza_type_id
GROUP BY 
    pt.category
ORDER BY 
    total_pizzas_sold DESC;
```
- Classic 22399
- Supreme 18137
- Veggie 17636
- Chicken 16643

### 6. Top 5 Best Sellers by Total Pizzas Sold
```javascript
SELECT 
    pt.name AS pizza_name,
    SUM(od.quantity) AS total_pizzas_sold
FROM 
    order_details od
JOIN 
    pizzas p ON od.pizza_id = p.pizza_id
JOIN 
    pizza_types pt ON p.pizza_type_id = pt.pizza_type_id
GROUP BY 
    pt.name
ORDER BY 
    total_pizzas_sold DESC
LIMIT 5;
```
- The Classic Deluxe Pizza 2453
- The Barbecue Chicken Pizza 2432
- The Hawaiian Pizza 2422
- The Pepperoni Pizza 2418
- The Thai Chicken Pizza 2371

### 7. Bottom 5 Worst Sellers by Total Pizzas Sold
```javascript
SELECT 
    pt.name AS pizza_name,
    SUM(od.quantity) AS total_pizzas_sold
FROM 
    order_details od
JOIN 
    pizzas p ON od.pizza_id = p.pizza_id
JOIN 
    pizza_types pt ON p.pizza_type_id = pt.pizza_type_id
GROUP BY 
    pt.name
ORDER BY 
    total_pizzas_sold ASC
LIMIT 5;
```
- The Brie Carre Pizza 490
- The Mediterranean Pizza 934
- The Calabrese Pizza 937
- The Spinach Supreme Pizza 950
- The Soppressata Pizza 961






