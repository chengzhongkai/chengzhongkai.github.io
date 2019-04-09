#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import time
import threading
import serial
import sys
from serial.tools.list_ports import comports
import logging
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def handle_data(data):
    print(data)

def read_from_port(ser,logger):
  while True:
    reading = ser.read_until('\r').decode()
    if len(reading) >0 :
      sys.stdout.write(reading)
      sys.stdout.flush()
      logger.info(ser.name+":"+reading.replace('\r', '\\r').replace('\n', '\\n'))
    #handle_data(reading)

def write_to_port(ser,logger):
  while True:
    ser.write(b"hello")
    time.sleep(3)

def main():

  # define args
  parser = argparse.ArgumentParser()
  parser.add_argument('com',type=str)
  parser.add_argument('-l', "--logfile", type=str, default='uartLog.log')
  args = parser.parse_args()

  # check args
  #   get ports list
  ports = []
  for n, (port, desc, hwid) in enumerate(sorted(comports()), 1):
    #sys.stderr.write('--- {:2}: {:20} {!r}\n'.format(n, port, desc))
    ports.append(port)
  if not args.com in ports:
    print(ports)
    print("com name error.\r\n")
    exit()
  
  # open uart port
  port = args.com
  baud = 115200
  serial_port = serial.Serial(port, baud, timeout=0.1)
  
  # create logger
  logger = logging.getLogger(__name__)
  fmt = "%(asctime)s %(levelname)s %(name)s :%(message)s"
  logging.basicConfig(filename=args.logfile,level=logging.DEBUG, format=fmt)
  thread = threading.Thread(target=read_from_port, args=(serial_port,logger))
  thread.start()

if __name__ == "__main__":
    main()
