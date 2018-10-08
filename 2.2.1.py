prix = int(input('Prix: '))

if prix > 500:
  prix *= 0.92
elif prix > 100:
  prix *= 0.95

print('Prix après remise: ', prix)
