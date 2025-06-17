# 🚲 Bike Rental Dashboard

A data visualization dashboard built with **Streamlit**, **Pandas**, **Seaborn**, and **Matplotlib** to analyze bike rental user data from the years **2011** and **2012**. The dashboard displays insights based on date, weather, and season using dynamic filtering and interactive plots.

---

## 📁 Project Structure
.
├── main_dashboard.py   # Main Streamlit dashboard code  
├── new_day.csv         # Preprocessed dataset (expected in same folder)  
└── README.md           # Project documentation  


---

## 📊 Features

- Interactive date filtering sidebar
- Summary metrics:
  - Total users
  - Highest / Lowest user records
  - Average users
- Line charts of daily and monthly user trends
- Season and weather breakdown for:
  - 2011 users
  - 2012 users
- Custom color highlights for most active categories

---
## 📅 Dataset Notes

- Dataset is read from `new_day.csv`
- Must contain at least the following columns:
  - `dteday`: date in a `YYYY-MM-DD` format
  - `yr`: year (`0` = 2011, `1` = 2012)
  - `cnt`: total users
  - `season`: season code (`1` = spring, `2` = summer, `3` = autumn, `4` = winter)
  - `weathersit`: weather code (`1` = clear, `2` = mist, `3` = slightly bad, `4` = very bad)

---

## 📈 Example Visualizations

- 📆 **Line chart**: Monthly user trends in 2011 & 2012
- 🌦️ **Bar charts**: Total rentals per season and weather
- 📊 **Metrics**: Automatically calculated for filtered data

---

## Setup environment
```
pipenv install
pipenv shell
pip install pandas matplotlib seaborn jupyter streamlit
```

---

## Run steamlit app
```
streamlit run main_dashboard.py
```

---

## Deploy streamlit link
'''
https://projectdashboardpy-7wwr8tduddccqumx49njk7.streamlit.app/
'''
---
## ✨ Possible Enhancements

- Add support for hour-level filtering
- Include user type breakdown (e.g., casual vs. registered)
- Export plots to PDF or image formats
- Deploy to cloud (Streamlit Community Cloud or Heroku)

---

## 📄 License

This project is released under the **MIT License**.

---

## 👤 Author

**Roy Indra Pratama**  
GitHub: [@RoyIndr](https://github.com/RoyIndr)
