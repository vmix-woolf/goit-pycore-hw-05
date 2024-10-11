def display_log_counts(counts: dict):
    '''Outputs overall statistics for all error levels'''
    print(f"\n{'Logging level':<20}", "|", f"{'Count':<10}", sep="")
    print(f"-" * 20 + "|" + f"-" * 10)

    for level, qty in counts.items():
        print(f"{level.upper():<20}", "|", f"{qty:<10}", sep="")
