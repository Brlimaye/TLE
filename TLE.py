# The script uses String Parsing method. Thus no extra package/module/library is required.
# Thanks!!

inp=input('TLE line 1:\n')
inp2=input('TLE line 2:\n')
split_input=inp.split(' ')
f_split_input=[]
for elem in range (0, len(split_input)):
  if split_input[elem] != '':
    f_split_input.append(split_input[elem])
  else:
    pass
split_input2=inp2.split(' ')
f_split_input2=[]
for elem2 in range (0, len(split_input2)):
  if split_input2[elem2] != '':
    f_split_input2.append(split_input2[elem2])
  else:
    pass
print("Results -->\n")
print('Line Number: ' + f_split_input[0])
print('Satellite Catalog Number: '+f_split_input[1][:5])
if f_split_input[1][5]=='U':
  print('Classification: Unclassified)')
elif f_split_input[1][5]=='C':
  print('Classification: Classified')
else:
  print('Classification: Secret')
print('International Designator(last 2 digits of launch year): '+
  f_split_input[2][:2])
print('International Designator(launch number of the year): '+
  f_split_input[2][2:5])
print('International Designator(piece of the launch): '+
  f_split_input[2][5:])
print('Epoch Year (last 2 digits of Year): '+f_split_input[3][:2])
print('Epoch (day of the year and fractional portion of the day): '+f_split_input[3][2:])
print('First Derivative of mean motion; the Ballistic Coefficient: '+ f_split_input[4])
print('Second Time Derivative of mean motion (decimal point assumed): '+f_split_input[5])
print('B* Drag term / radiation pressure coefficient (decimal point assumed): '+ f_split_input[6], end='  ->  ')
print('0.' +f_split_input[6][:5], end='e')
print(f_split_input[6][-2:])
print('Ephemeris Type: '+f_split_input[7])
print('Element set number: '+f_split_input[8][:3])
print('Checksum: '+f_split_input[8][-1]+ " (modulo 10)")
print('------------------------  -------------------------')
print('Line Number: ' + f_split_input2[0])
print('Satellite Catalog Number: '+f_split_input2[1][:5])
print('Inclination (degrees): '+f_split_input2[2]+ "°")
print('Right ascension of the ascending node (degrees): '+f_split_input2[3]+"°")
print('Eccentricity (decimal point assumed): '+'.'+f_split_input2[4])
print('Argument of Perigee (degrees): '+f_split_input2[5]+"°")
print('Mean Anomaly (degrees): '+f_split_input2[6]+"°")
print('Mean Motion (revolutions/day): '+f_split_input2[7][:11] +" revolutions/day")
print('Revolution number at Epoch (revolutions): '+f_split_input2[7][11:16]+" revolutions")
print('Checksum: '+f_split_input2[7][-1]+" (modulo 10)")