import sys
from loader import load_logs
from parse_log_line import parse_log_line
from filter_logs import filter_logs_by_level
from count_logs import count_logs_by_level
from display_counts import display_log_counts
from display_level import display_logs_level


def log_analyzer():
    _, *args = sys.argv
    file_name = args[0]
    
    try:
        level = args[1]
    except IndexError:
        print(f"There is no extra parameter. Displaying a full statistics.")
        level = None  
    lines = load_logs(file_name)
    
    dictionary = {}
    total_list = []
    
    for line in lines:
        dictionary = parse_log_line(line)
        total_list.append(dictionary)
    
    counts = count_logs_by_level(total_list)
    display_log_counts(counts)
    
    if level:
        filtered_logs_list = filter_logs_by_level(total_list, level)
        display_logs_level(filtered_logs_list, level)


if __name__ == "__main__":
    log_analyzer()
