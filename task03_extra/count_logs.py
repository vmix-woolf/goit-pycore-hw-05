def count_logs_by_level(logs: list) -> dict:
    counts = {
        'info': 0,
        'warning': 0,
        'debug': 0,
        'error': 0,
    }

    for log in logs:
        if log['level'] == 'INFO':
            counts['info'] += 1
        elif log['level'] == 'WARNING':
            counts['warning'] += 1
        elif log['level'] == 'DEBUG':
            counts['debug'] += 1    
        elif log['level'] == 'ERROR':
            counts['error'] += 1
    
    return counts
