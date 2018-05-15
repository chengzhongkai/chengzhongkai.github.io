#coding:utf-8
from __future__ import print_function	# python3.x系では不要
import io
import serial
from serial.tools import list_ports
import sys

"""
参考URL: pyserial公式ドキュメント
[1]サイトトップ http://pythonhosted.org/pyserial/
[2]API一覧 http://pythonhosted.org/pyserial/pyserial_api.html
[3]イントロダクション http://pythonhosted.org/pyserial/shortintro.html
"""

if __name__ == "__main__":
	ser = serial.Serial()
	ser.baudrate = 9600	# ArduinoのSerial.beginで指定した値
	ser.timeout = 0.1		# タイムアウトの時間

	ports = list_ports.comports()	# ポートデータを取得
	
	devices = []
	for info in ports:
		devices.append(info.device)	# ポートの名前を取得

	if len(devices) == 0:
		# シリアル通信できるデバイスが見つからなかった場合
		print("error: device not found")
		sys.exit(0)
	elif len(devices) == 1:
		ser.port = devices[0]	# ポートを指定
	else:
		# ポートが複数見つかった場合
		# "COM1"とか"COM3"とかを表示する
		for i in range(len(devices)):
			print("input " + str(i)+":\topen "+devices[i])
		
		# 開くポートを指定する
		print("input number of target port\n>> ",end="")
		num = int(raw_input())
		ser.port = devices[num]	# ポートを指定
	
	# 開いてみる
	try:
		ser.open()
		print("open " + ser.port )
	except:
		print("can't open" + ser.port )
		sys.exit(0)

	# readlineを使うためのもの
	sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
	
	# ちゃんと開けていたらループに入る
	while ser.is_open:
		s = sio.readline()	# 1行読み込む
		if s != "":
			print("\n" + s , end="")
		else:
			print(".",end="")

	print("serial connection closed")
	