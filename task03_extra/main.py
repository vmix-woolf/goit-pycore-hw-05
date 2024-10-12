import sys
from load_logs import load_logs
from parse_log_line import parse_log_line
from filter_logs import filter_logs_by_level
from count_logs_by_level import count_logs_by_level
from display_logs_counts import display_log_counts
from display_logs_level import display_logs_level


def log_analyzer():
    '''Analyzes the log file'''
    _, *args = sys.argv
    try:
        file_name = args[0]
    except IndexError:
        print(f"Don't forget to enter the correct log file path and name")
        exit()
    
    try:
        level = args[1]
        if level not in ['error', 'info', 'debug', 'warning']:
            raise ValueError
    except IndexError:
        level = None
    except ValueError:
        print(f"No such information level")
        exit()  
    
    lines = load_logs(file_name)
    
    parsed_line = {}
    parsed_lines = []
    for line in lines:
        parsed_line = parse_log_line(line)
        parsed_lines.append(parsed_line)

    counts = count_logs_by_level(parsed_lines)
    display_log_counts(counts)
    
    if level:
        filtered_logs_list = filter_logs_by_level(parsed_lines, level)
        display_logs_level(filtered_logs_list, level)


if __name__ == "__main__":
    log_analyzer()
