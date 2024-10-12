import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
import joblib

class ModelTrainer:
    def __init__(self, model_path='trained_model.pkl', scaler_path='scaler.pkl'):
        self.model_path = model_path
        self.scaler_path = scaler_path
        self.model = None
        self.scaler = None

    def train_model(self, df):
        features = ['Response Time', 'Status Code', 'Content Length']
        self.scaler = StandardScaler()
        df[features] = self.scaler.fit_transform(df[features])

        contamination_rate = 0.05
        self.model = IsolationForest(contamination=contamination_rate, random_state=42)
        self.model.fit(df[features])

        joblib.dump(self.model, self.model_path)
        joblib.dump(self.scaler, self.scaler_path)

    def load_model(self):
        self.model = joblib.load(self.model_path)
        self.scaler = joblib.load(self.scaler_path)

    def predict(self, data):
        features = ['Response Time', 'Status Code', 'Content Length']
        data[features] = self.scaler.transform(data[features])
        return self.model.predict(data[features])
