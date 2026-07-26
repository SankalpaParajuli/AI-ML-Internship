"""
Simple File Parser
--------------------
Parses a text log file and extracts useful statistics/information.
Demonstrates: file I/O, string processing, dictionaries, functions.

The script generates a sample log file (server_log.txt) if one doesn't
exist, then parses it to report line counts, word frequency, and
level-based counts (INFO / WARNING / ERROR) - similar to log parsing
tasks common in real backend/ML pipelines.
"""

import os
from collections import Counter

LOG_FILE = "server_log.txt"

SAMPLE_LOG = """\
INFO 2026-07-01 09:00:01 Server started successfully
INFO 2026-07-01 09:01:15 User sankalpa logged in
WARNING 2026-07-01 09:05:42 High memory usage detected
ERROR 2026-07-01 09:07:03 Failed to connect to database
INFO 2026-07-01 09:10:00 Retrying database connection
INFO 2026-07-01 09:10:05 Database connection restored
WARNING 2026-07-01 09:15:30 Disk space running low
ERROR 2026-07-01 09:20:11 Unhandled exception in module X
INFO 2026-07-01 09:25:00 User sankalpa logged out
INFO 2026-07-01 09:30:00 Server shutting down
"""


def create_sample_log(filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(SAMPLE_LOG)


def parse_log(filename):
    """Parse the log file into a list of dicts: level, date, time, message."""
    entries = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(" ", 3)
            if len(parts) < 4:
                continue
            level, date, time, message = parts
            entries.append({
                "level": level,
                "date": date,
                "time": time,
                "message": message
            })
    return entries


def summarize(entries):
    level_counts = Counter(entry["level"] for entry in entries)

    all_words = " ".join(entry["message"] for entry in entries).lower().split()
    word_freq = Counter(all_words)

    return level_counts, word_freq


if __name__ == "__main__":
    if not os.path.exists(LOG_FILE):
        create_sample_log(LOG_FILE)

    entries = parse_log(LOG_FILE)
    print(f"Parsed {len(entries)} log entries from '{LOG_FILE}'\n")

    level_counts, word_freq = summarize(entries)

    print("Log level counts:")
    for level, count in level_counts.items():
        print(f"  {level}: {count}")

    print("\nTop 5 most common words in messages:")
    for word, count in word_freq.most_common(5):
        print(f"  {word}: {count}")

    print("\nAll ERROR entries:")
    for entry in entries:
        if entry["level"] == "ERROR":
            print(f"  [{entry['date']} {entry['time']}] {entry['message']}")
