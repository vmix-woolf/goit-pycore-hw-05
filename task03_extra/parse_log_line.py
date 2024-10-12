import re

def parse_log_line(line: str) -> dict:
    record = {}
    
    date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')  # regexp for date
    time_pattern = re.compile(r'\d{2}:\d{2}:\d{2}')  # regexp for time
    level_pattern = re.compile(r'[A-Z]+')            # regexp for level
    message_pattern = re.compile(r"(.*?\s.*?\s.*?)\s")  # regexp for sentence
    
    record['date'] = re.search(date_pattern, line).group()  
    record['time'] = re.search(time_pattern, line).group()  
    record['level'] = re.search(level_pattern, line).group()  
    slice_of_line = line[re.search(message_pattern, line).span()[1]:]  # from found index till the end
    record['message'] = slice_of_line.strip()  # delete ending \n
    
    return record
