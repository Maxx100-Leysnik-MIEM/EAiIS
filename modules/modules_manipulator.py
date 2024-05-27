import time

import RPi.GPIO as GPIO
from ws_barcode_scanner import BarcodeScanner
import rdm6300
from customMFRC522 import CustomMFRC522
import config

#TODO create custom MFRC522: exit while reading
def readNFC():
    try:
        print("Start")
        reader = CustomMFRC522(config.KEY, config.BLOCK_ADDRS)
        id, text = reader.read()
        print("id:", id, "txt:", text)
        reader.READER.spi.close()
        return id, text
    except KeyboardInterrupt:
        reader.READER.spi.close()
        GPIO.cleanup()
        raise
        

def scanBarcode():
    scanner = BarcodeScanner("COM3")

    #TODO while loop until correct timestamp 
    res = scanner.query_for_codes()
    return res[-1]

def readRFID():
    reader = rdm6300.Reader('/dev/serial0') #/dev/serial0 or /dev/tty0
    print("Please insert an RFID card")
    end_time = time.time() + config.WAIT_TIME
    while end_time >= time.time():
        card = reader.read()
        if card:
            print(f"[{card.value}] read card {card}")
            return card
    return -1