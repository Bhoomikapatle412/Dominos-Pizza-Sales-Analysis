 🍕 Domino's Pizza Sales Analysis

An end-to-end **Data Analytics** project built using **Python**, **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn** to analyze Domino's pizza sales data. This project focuses on data cleaning, preprocessing, exploratory data analysis (EDA), visualization, and extracting business insights from real-world sales data.


📌 Project Overview

The objective of this project is to analyze Domino's pizza sales data to identify customer preferences, sales trends, and revenue patterns. The project demonstrates the complete data analysis workflow, from raw datasets to actionable business insights.


🎯 Objectives

- Acquire and preprocess sales data
- Clean and validate datasets
- Merge multiple datasets into a unified dataset
- Perform Exploratory Data Analysis (EDA)
- Create meaningful visualizations
- Generate business insights for decision-making

 🗂 Dataset Information

The analysis uses three CSV files:

| Dataset | Description |
|----------|-------------|
| `order_details.csv` | Contains order IDs, pizza IDs, and quantities ordered |
| `pizzas.csv` | Contains pizza sizes, prices, and pizza type IDs |
| `pizza_types.csv` | Contains pizza names, categories, and ingredients |

After preprocessing and merging, the final dataset contains:

- **48,620 Rows**
- **10 Columns**

🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Visual Studio Code
- Git & GitHub


📊 Exploratory Data Analysis

The following business questions were explored:

- Which pizzas are ordered the most?
- Which pizza size is most popular?
- Which pizza category sells the most?
- Which category generates the highest revenue?
- Which pizzas generate the highest revenue?
- What is the correlation between numerical variables?
- How is the quantity sold distributed?
- How is revenue distributed?

📈 Visualizations

This project includes the following visualizations:

- Top 10 Best Selling Pizzas
- Quantity Sold by Pizza Size
- Total Quantity Sold by Pizza Category
- Revenue by Pizza Category
- Top 10 Revenue Generating Pizzas
- Correlation Heatmap
- Quantity Distribution Histogram
- Revenue Distribution Box Plot

All generated graphs are available in the **graphs/** folder.

📌 Key Business Insights

- Large (L) pizzas are the most frequently ordered size.
- Classic pizzas recorded the highest sales quantity.
- Classic pizzas also generated the highest overall revenue.
- Thai Chicken Pizza generated the highest revenue among all pizzas.
- Revenue has a strong positive correlation with price.
- Most customers purchase only one pizza per order.
- Premium pizzas contribute significantly to overall revenue.


📂 Project Structure

Dominos-Pizza-Sales-Analysis/
│
├── Dataset/
│   ├── order_details.csv
│   ├── pizzas.csv
│   └── pizza_types.csv
│
├── graphs/
│   ├── top_10_best_selling_pizzas.png
│   ├── pizza_size_sales.png
│   ├── category_sales.png
│   ├── revenue_by_category.png
│   ├── top_10_revenue_pizzas.png
│   ├── correlation_heatmap.png
│   ├── quantity_distribution.png
│   └── revenue_distribution_boxplot.png
│
├── report/
│   └── Domino_Pizza_Sales_Report.pdf
│
├── main.py
├── requirements.txt
└── README.md


▶️ How to Run the Project

### Clone the repository

```bash
git clone https://github.com/Bhoomikapatle412/Dominos-Pizza-Sales-Analysis.git
```

### Navigate to the project folder

```bash
cd Dominos-Pizza-Sales-Analysis
```

### Install the required libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### Run the project

```bash
python main.py
```

---

📷 Sample Output

The project generates multiple visualizations and business reports, including:

- Sales trends by pizza type
- Revenue analysis
- Category performance
- Customer ordering behavior
- Correlation analysis

---

🚀 Future Enhancements

- Develop an interactive Power BI dashboard
- Build a Tableau dashboard
- Predict future sales using Machine Learning
- Perform customer segmentation
- Analyze seasonal sales trends
- Deploy the project using Streamlit

---

👩‍💻 Author

Bhoomika Patle

Computer Science Engineering (AI & ML)

GitHub: https://github.com/Bhoomikapatle412


⭐ If you found this project useful, consider giving it a star!
