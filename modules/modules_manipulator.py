from time import sleep
import sys

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from ws_barcode_scanner import BarcodeScanner
import rdm6300

#TODO create custom MFRC522: authKey, exit while reading
def readNFC():
    try:
        reader = SimpleMFRC522()
        id, text = reader.read()
    except KeyboardInterrupt:
        GPIO.cleanup()
        raise

def scanBarcode():
    scanner = BarcodeScanner("COM3")
    #TODO while loop until correct timestamp 
    res = scanner.query_for_codes()
    return res[-1]

def readRFID():
    reader = rdm6300.Reader('/dev/serial0')
    print("Please insert an RFID card")
    while True:
        card = reader.read()
        if card:
            print(f"[{card.value}] read card {card}")
            return card



