def count_logs_by_level(logs: list) -> dict:
    '''Counts the number of records with records of a certain information level'''
    counts = {
        'info': 0,
        'warning': 0,
        'debug': 0,
        'error': 0,
    }

    for log in logs:
        match log['level']:
            case 'INFO': counts['info'] += 1
            case 'WARNING': counts['warning'] += 1
            case 'DEBUG': counts['debug'] += 1
            case 'ERROR': counts['error'] += 1

    return counts
