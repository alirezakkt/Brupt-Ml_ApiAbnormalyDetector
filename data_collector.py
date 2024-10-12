from burp import IResponseInfo

class DataCollector:
    def __init__(self, helpers):
        self.helpers = helpers

    def collect_data(self, baseRequestResponse):
        response_info = self.helpers.analyzeResponse(baseRequestResponse.getResponse())
        response_time = baseRequestResponse.getResponseTime()
        status_code = response_info.getStatusCode()
        content_length = len(baseRequestResponse.getResponse())

        auth_token = 1 if 'Authorization' in str(response_info.getHeaders()) else 0

        return {
            'Response Time': response_time / 1000.0,  # Convert to seconds
            'Status Code': status_code,
            'Content Length': content_length,
            'Auth Token': auth_token
        }
