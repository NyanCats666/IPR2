import gzip
import re

Test = open("TestFileWriter", "w", encoding="utf-8")
with gzip.open('csv_example.csv.gz', 'rb') as f:
    # line = f.readline()
    for i, line in enumerate(f):
        print(line)
        mount = (re.search(r'[A-Z]{1}[a-z]{2}', str(line))).group(0)
        day = (re.search(r'[0-9]{1}', str(line))).group(0)
        time = (re.search(r'[0-9]{2}:[0-9]{2}:[0-9]{2}', str(line))).group(0)
        logIn = (re.search(r'[a-z,0-9]{15}', str(line))).group(0)
        serName = (re.search(r'esia.gos.*?\s', str(line))).group(0)
        timeStamp = (re.search(r'[0-9]{2}\/[A-Z]{1}[a-z]{2}\/[0-9]{4}:[0-9]{2}:[0-9]{2}:[0-9]{2}', str(line))).group(0)
        lat = (re.search(r'\+[0-9]{4}', str(line))).group(0)
        ip = (re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', str(line))).group(0)
        lat = (re.search(r'\+[0-9]{4}', str(line))).group(0)
        restMethod = (re.search(r'[A-Z]{4}|[A-Z]{3}', str(line))).group(0)
        restPath = (re.search(r'\/[a-z].*?\s', str(line))).group(0)
        HTTPver = (re.search(r'HTTP.*?\s', str(line))).group(0)
        prochee = re.sub(r' ', '|', ((re.search(r'".*"', str(line))).group(0)))
        responceTime = (re.search(r'upst.+?[0-9].+?[0-9].+|upst.+?[0-9].+?[0-9].+?\n|upst.+?\n|upst.+?-', str(line))).group(0)
        # if re.match(r'\\n', responceTime):
        print(responceTime)
        Test.write(mount + "|" + day + "|" + time + "|" + logIn + "|" + serName + "|" + timeStamp + "|" +
                   lat + "|" + ip + "|" + restMethod + "|" + restPath + "|" + HTTPver + "|" + prochee + "|" + responceTime + '\n')
Test.close()
