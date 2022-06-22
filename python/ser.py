import serial
import time


def main():
  ser = serial.Serial("COM3", 115200, timeout=None)
  (func, group, comm) = (1, 1, 30)
  id = [1, 2, 3, 4]
  i = 1
  try:
    while 1:
      message = (str(func)+","+str(group)+","+str(id[i-1])+","+str(comm)).encode('utf-8')
      ser.write(message)
      i = (i + 1) % len(id)
      comm = (comm + 50) % 1000
      time.sleep(2)
      print(message)
  except KeyboardInterrupt:
    for i in id:
      time.sleep(1.5)
      message = (str(func)+","+str(group)+","+str(i)+","+str(0)).encode('utf-8')
      ser.write(message)
      print(message)
    time.sleep(1.5)
  ser.close()
  return
  

if __name__ == '__main__':
  main()
