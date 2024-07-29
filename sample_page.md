## SQL

## Pizza

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


### 4. Provide a basis for further data collection through surveys or experiments

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. 

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).
