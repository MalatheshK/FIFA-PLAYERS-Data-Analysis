from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
  df_20, df_19, df_18, df_17, df_16, df_15 = load_data()
  data_display_20 = data_display(df_20)
  data_display_19 = data_display(df_19)
  data_display_18 = data_display(df_18)
  data_display_17 = data_display(df_17)
  data_display_16 = data_display(df_16)
  data_display_15 = data_display(df_15)
  return render_template('home.html', data_20=data_display_20, data_19=data_display_19, data_18=data_display_18, 
                         data_17=data_display_17, data_16=data_display_16, data_15=data_display_15)

def load_data():
  df_20 = pd.read_csv('Dataset/players_20.csv')
  df_19 = pd.read_csv('Dataset/players_19.csv')
  df_18 = pd.read_csv('Dataset/players_18.csv')
  df_17 = pd.read_csv('Dataset/players_17.csv')
  df_16 = pd.read_csv('Dataset/players_16.csv')
  df_15 = pd.read_csv('Dataset/players_15.csv')
  return df_20, df_19, df_18, df_17, df_16, df_15

def data_display(df):
  display_data = df[['short_name', 'long_name', 'club', 'overall', 'potential', 'value_eur', 'wage_eur', 'player_positions',
                     'player_tags', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic',
                     'player_traits']].head(100).to_dict(orient='records')
  return display_data

if __name__ == '__main__':
  app.run(debug=True)