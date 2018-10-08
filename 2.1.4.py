seconds = 12334

hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

print("{hours}h {minutes}min and {seconds}s".format(hours=hours, minutes=minutes, seconds=seconds))
