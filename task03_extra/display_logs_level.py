def display_logs_level(filtered_logs: list, level: str):
    '''Outputs detailed statistics only for the corresponding error level'''
    print(f"\nLogging details for the level {level.upper()}")
    
    for log in filtered_logs:
        print(f"{log['date']} {log['time']} - {log['message']}")
