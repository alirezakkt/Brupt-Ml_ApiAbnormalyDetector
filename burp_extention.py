from burp import IBurpExtender, IScannerCheck
from src.data_collector import DataCollector
from src.model_training import ModelTrainer
from src.anomaly_detector import AnomalyDetector
from src.report_generator import ReportGenerator

class BurpExtender(IBurpExtender, IScannerCheck):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("API Behavioral Anomaly Detector")
        callbacks.registerScannerCheck(self)

        self.data_collector = DataCollector(self._helpers)
        self.model_trainer = ModelTrainer()
        self.report_generator = ReportGenerator()
        self.anomaly_detector = AnomalyDetector(self.model_trainer)

        self.model_trainer.load_model()
        print("API Anomaly Detector loaded and ready to use.")

    def doPassiveScan(self, baseRequestResponse):
        collected_data = self.data_collector.collect_data(baseRequestResponse)
        if collected_data is None:
            return None

        if self.anomaly_detector.detect_anomaly(collected_data):
            self.report_generator.log_anomaly(collected_data, "Anomaly detected")
            print("Anomaly detected and logged.")

        return None
