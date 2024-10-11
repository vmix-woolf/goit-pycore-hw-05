from pathlib import Path

def load_logs(file_path: str) -> list:
    '''Loads file as a list of lines'''
    current_dir = Path(__file__).parent
    
    try:
        with open(current_dir / file_path, mode='r', encoding='utf-8') as fh:
            lines = fh.readlines()
    except IOError:
        print(f"There is no such file. Enter the correct name of the log file.")
        exit()
    
    return lines
