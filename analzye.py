import pandas as pd
import sqlite3

connection = sqlite3.connect("data/wait_times_data.db")

query = """
SELECT "Data year", "Indicator result" 
FROM wait_times
WHERE "Indicator" = ?
    AND "Metric" = ?
ORDER BY "Data year";
"""

results = pd.read_sql_query(
    query, 
    connection,
    params=("Knee Replacement", "50th percentile")
)

connection.close()

print(results)