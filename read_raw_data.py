import pandas as pd

url = "https://worldpopulationreview.com/country-rankings/most-educated-countries"

def read_html_data():
    df_educ = pd.read_html(url)[2]
    
    return df_educ.head()  

