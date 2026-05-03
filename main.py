from schemas import raw_events
from date_processor import process_data 
from report_generator import generate_report as gen_func 

class ViolationAnalyzer:
    def __init__(self):
        self.df = None

    def load_events(self, data):
        # 這裡會呼叫 date_processor 裡的 process_data
        self.df = process_data(data)

    
    def generate_report(self):
        data_as_list = self.df.to_dict('records')
        result_message = gen_func(data_as_list) 
        print(result_message) # 加入這行，讓它執行完會講話
        return result_message
        

analyzer = ViolationAnalyzer()
analyzer.load_events(raw_events)
analyzer.generate_report()