#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""semihostLog.py: Save semihost output to a file."""

__author__      = "cheng"
__copyright__   = "Copyright 2019, Planet Earth"

import argparse
import time
import threading
import subprocess
import shlex
import sys
import logging
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


def run_command(command,logger):
  try:
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
  except FileNotFoundError:
    print('Path ERROR.')
    print('Please run in OpenOCD bin fold.')
    print('You can download OpenOCD in https://github.com/gnu-mcu-eclipse/openocd/releases.')
    return
  while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:
      break
    if output:
      print('->',output.strip())
      logger.info(output.strip())
  rc = process.poll()
  return rc

def read_from_semi(ss, logger):
  run_command('./openocd -f ../scripts/interface/jlink.cfg -c "transport select swd" -f ../scripts/target/kl46.cfg -c "init; reset run;arm semihosting enable;resume"',logger)

def main():

  # define args
  parser = argparse.ArgumentParser()
  parser.add_argument('-l', "--logfile", type=str, default='semihost.log')
  parser.add_argument('-i', "--interface", type=str, default='jlink')
  parser.add_argument('-t', "--target", type=str, default='kl46')
  args = parser.parse_args()

  # check args
  
  # create logger
  logger = logging.getLogger(__name__)
  fmt = "%(asctime)s %(levelname)s :%(message)s"
  logging.basicConfig(filename=args.logfile,level=logging.DEBUG, format=fmt)
  thread = threading.Thread(target=read_from_semi, args=(' ',logger))
  thread.start()

if __name__ == "__main__":
    main()
