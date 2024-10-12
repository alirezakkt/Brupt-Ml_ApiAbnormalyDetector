Use Jyton 2.7.2 Env
# Brupt-Ml_ApiAbnormalyDetector
In this Repo i try to make a API Vulnerabilty Scanner while working on target 


his project is a **Burp Suite Extension** that automatically collects API traffic, logs it, and uses machine learning models to detect potential anomalies and vulnerabilities in API requests. The tool is designed to streamline API security testing and enhance the detection of unusual or insecure API behavior.

## Features

- **Automatic API Traffic Collection**: Collects API requests in real-time and stores them in a CSV format.
- **Machine Learning Model Training**: Prompts the user to train a machine learning model based on collected API data.
- **Anomaly Detection**: Uses the trained model to detect anomalous API requests.
- **API Vulnerability Testing**: Once trained, the model assists in identifying potential vulnerabilities in APIs.
- **Parallel API Request Handling**: Collects API requests in parallel for better performance.

- How It Works
API Traffic Collection: All incoming and outgoing API requests are captured by the data_collector.py module and saved for analysis.
Model Training: Once enough data is collected, the user is prompted to train a machine learning model using scikit-learn to classify requests and identify unusual patterns.
Anomaly Detection: The trained model is used to flag potential anomalies in subsequent API traffic, allowing for quick identification of security flaws.

