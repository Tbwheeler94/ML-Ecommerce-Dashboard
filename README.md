# ML-Ecommerce-Dashboard

## Project Overview

Improving predictions of customer behavior online can have a substantial impact on business and marketing strategy for ecommerce companies. This project uses a dataset from Brazilian e-commerce company Olist to explore 2 potentially consequential predictions: 

(1) Will a customer make a repeat purchase? <br>
(2) Will a customer's review be positive or negative based on the product listing?

To develop predictions we trained our dataset on using 2 machine-learning algorithms:

(1) Logisitic regression <br>
(2) Random forest classification

This dashboard allows the user to explore the algorithms' predictions by allowing the user to adjust input parameters and see how the prediction changes. Ultimately these models help the user better understand what factors have the most impact on customer decision-making.

[Link to website](https://lazuli-ecom-machine-learning.herokuapp.com/)

## Data Analysis

To assess customer decision making, we used the following parameters for each question:

### Q1: Will the customer make a repeat purchase?

Parameters:

- How Many Total Delivery Days Were Required: Number of Days (Integer)
- How Many Days Early or Late Was The Order: Number of Days (Integer)
- What Was The Customer's Review Score?: Number of Stars out of 5 (Integer)
- Was the Shipment Late?: Yes or No (Boolean)

Analysis method: logistic regression

[](https://github.com/Tbwheeler94/ML-Ecommerce-Dashboard/blob/main/readme_gifs/repeat_purchase.gif)

### Q2: Will the customer leave a positive or negative review?

Parameters:

- Product Description Length: Number of Words (Integer)
- Quantity of Photos: Number of Photos (Integer)
- Is it Late?: Yes or No (Boolean)
- Payment Type: Select type (Ordinal)
- Total Order Value: $ (Integer)

Analysis method: random forest classification

[](https://github.com/Tbwheeler94/ML-Ecommerce-Dashboard/blob/main/readme_gifs/predict_review.gif)

## Data Source

Dataset sourced from kaggle.com, original from [Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) a Brazilian e-commerce company.

## Credits

This project was developed in partnership with 4 other students (see "About" page) as my final project for completion of [University of California, San Diego's Data Science Bootcamp](https://bootcamp.extension.ucsd.edu/data/).
