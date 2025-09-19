# Buenos Aires Apartment Price Prediction
    # Predicting Price with Size
    
## 📌 Project Overview
This project is credited to World Quant University an online course session where we build a **linear regression model** to predict the price of apartments in Buenos Aires, focusing only on properties under $400,000 USD located in *Capital Federal*. 
The aim is to practice reproducible data cleaning, exploratory data analysis, baseline modelling, and linear regression evaluation.

---

## 🎯 Objectives
1. Import and clean real estate datasets with a reusable function.
2. Remove outliers based on apartment size (surface_covered_in_m2).
3. Explore data distributions and relationships between size and price.
4. Establish a baseline model for comparison.
5. Train and evaluate a simple linear regression model.
6. Compare performance using **Mean Absolute Error (MAE)**.

---

## 🗂️ Project Structure
```
BuenosAires_AptPrice_Project/
│
├── data/
│   ├── raw/                # original CSV datasets
│   ├── processed/          # cleaned datasets
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   ├── 03_model_building.ipynb
│
├── scripts/
│   ├── wrangle.py          # import & cleaning functions
│   ├── train_model.py      # training pipeline
│
├── visuals/                # saved charts and figures
│
├── requirements.txt        # dependencies
└── README.md               # project documentation
```

---

## ⚙️ Setup Instructions
1. Clone/download this project folder.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # on macOS/Linux
   venv\Scripts\activate    # on Windows
   ```
3. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📊 Workflow
1. **Data Preparation**: Clean data with `wrangle.py` (filter price < $400k, remove outliers, keep only Capital Federal).
2. **Exploratory Analysis**: Visualise size distribution, scatter plots, and summary statistics.
3. **Baseline Model**: Predict average price and evaluate performance.
4. **Linear Regression Model**: Train on size vs. price, compare to baseline, compute MAE.
5. **Visualisation**: Plot regression line on scatter plot for better interpretation.

---

## ✅ Results
- Baseline prediction error (MAE): ~\$45,199
- Linear regression error (MAE): Improved by ~\$10,000
- Conclusion: Apartment size is a significant predictor of price.

---

## 🚀 Next Steps
- Add more features (e.g., location, number of rooms).
- Split data into training/test sets for better validation.
- Try more advanced models beyond linear regression.
