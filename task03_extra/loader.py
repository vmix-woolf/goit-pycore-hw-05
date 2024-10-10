from pathlib import Path

def load_logs(file_path: str) -> list:
    current_dir = Path(__file__).parent
    
    with open(current_dir / file_path, mode='r', encoding='utf-8') as fh:
        lines = fh.readlines()
    
    return lines
