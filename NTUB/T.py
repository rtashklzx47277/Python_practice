from datetime import datetime, timedelta
import sys
data = sys.stdin.read()

for days in data.splitlines()[1:]:
  print((datetime.strptime('1970-01-01', '%Y-%m-%d') + timedelta(days = int(days))).strftime(('%Y-%m-%d')))