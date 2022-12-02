from datetime import datetime, timezone, timedelta

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

print(today)
print(tomorrow)

print(today.strftime('%d-%m-%Y %H:%M.%f'))
print(today.strftime('%F %T.%f'))
