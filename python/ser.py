import serial
import time
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By

ser = serial.Serial("COM3", 115200, timeout=None)
(func, group, comm) = (1, 1, 30)
id = [1, 2, 3, 4]
# reference: https://www.seleniumqref.com/api/python/element_infoget/Python_text.html
chromeDriver = "D:\\Users\\USER\\AppData\\Local\\Programs\\chromedriver\\chromedriver.exe"
chromeService = service.Service(executable_path=chromeDriver)
driver = webdriver.Chrome(service=chromeService)
driver.get("https://atsunemogi.github.io/glow-voice-command/")


def glowOn():
  global func, group, comm, id
  for i in id:
    message = (str(func)+","+str(group)+","+str(i)+","+str(comm)).encode('utf-8')
    ser.write(message)
    comm = (comm + 50) % 1000
    time.sleep(2)
    print(message)
  return


def glowOff():
  global func, group, comm, id
  for i in id:
    time.sleep(1.5)
    message = (str(func)+","+str(group)+","+str(i)+","+str(0)).encode('utf-8')
    ser.write(message)
    print(message)
  time.sleep(2)
  return


def getContent():
  element = driver.find_element(By.ID, "content")
  text = element.text
  if (text == "yes"):
    print(text)
    glowOn()
  elif (text == "no"):
    print(text)
    glowOff()


def main():
  while(1):
    try:
      getContent()
      time.sleep(2)
    except KeyboardInterrupt:
      glowOff()
      break
  ser.close()
  

if __name__ == '__main__':
  main()
