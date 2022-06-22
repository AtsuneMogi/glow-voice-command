import serial
import time
import requests
from bs4 import BeautifulSoup

ser = serial.Serial("COM3", 115200, timeout=None)
(func, group, comm) = (1, 1, 30)
id = [1, 2, 3, 4]
i = 1


def glowOn():
  try:
    while 1:
      message = (str(func)+","+str(group)+","+str(id[i-1])+","+str(comm)).encode('utf-8')
      ser.write(message)
      i = (i + 1) % len(id)
      comm = (comm + 50) % 1000
      time.sleep(2)
      print(message)
  except KeyboardInterrupt:
    glowOff()
  ser.close()
  return


def glowOff():
  for i in id:
    time.sleep(1.5)
    message = (str(func)+","+str(group)+","+str(i)+","+str(0)).encode('utf-8')
    ser.write(message)
    print(message)
  time.sleep(1.5)


def main():
  while(1):
    getContent()
    time.sleep(2)


def getContent():
  url = "https://atsunemogi.github.io/glow-voice-command/"
  html = requests.get(url)
  soup = BeautifulSoup(html.content, "html.parser")
  command = soup.find(id="content").text
  if ((command == "one") or (command == "1")):
    glowOn()
  elif ((command == "zero") or (command == "0")):
    glowOff()


if __name__ == '__main__':
  main()
