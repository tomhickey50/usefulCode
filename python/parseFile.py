import os,re

if(os.path.exists('weatherData.txt')):
    with open('weatherData.txt', 'r') as f:
        txtData = f.readlines()
        for line in txtData:
            print(line)
            if "time" in line:
                txtTime = re.findall('\d+', line[6:])
            elif "windBearing" in line:
                txtBearing = re.findall('\d+', line[12:])
            elif "windSpeed" in line:
                txtHumidity = re.findall('\d.\d+', line[9:])
            elif "dewpt" in line:
                txtDew = re.findall('\d+.\d+', line[6:])
            elif "temp" in line:
                txtTemp = re.findall('\d+.\d+', line[5:])
#touch in python
else:
    with open('weatherData.txt', 'a'):
        os.utime('weatherData.txt', None)
