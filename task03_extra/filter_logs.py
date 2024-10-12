def filter_logs_by_level(logs: list, level: str = None) -> list:
    '''Selects records that match the desired error level'''
    return [ log for log in logs if log['level'] == level.upper() ]  # list comprehension usage
