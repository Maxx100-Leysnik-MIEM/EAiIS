import RPi.GPIO as GPIO
from ws_barcode_scanner import BarcodeScanner
import rdm6300
from customMFRC522 import CustomMFRC522
import config

def readNFC():
    try:
        reader = CustomMFRC522(config.KEY, config.BLOCK_ADDRS)
        id, text = reader.read()
        reader.READER.spi.close()
        return id, text
    except KeyboardInterrupt:
        reader.READER.spi.close()
        GPIO.cleanup()
        raise

def writeNFC(id_):
    try:
        mfrc = CustomMFRC522(config.KEY, config.BLOCK_ADDRS)
        id, text = mfrc.write(id_)
        mfrc.READER.spi.close()
        return id, text
    except KeyboardInterrupt:
        mfrc.READER.spi.close()
        GPIO.cleanup()
        raise

def scanBarcode():
    scanner = BarcodeScanner("COM3")

    #TODO while loop until correct timestamp 
    res = scanner.query_for_codes()
    return res[-1]

def readRFID():
    reader = rdm6300.Reader('/dev/ttyAMA0') #/dev/serial0 or /dev/tty0 or /dev/ttyAMA0 ot /dev/ttyACM0
    card = reader.read(config.WAIT_TIME)
    if card:
        print(f"[{card.value}] read card {card}")
        return card
    else:
        return -1
    
if __name__ == "__main__":
    while True:
        print(readRFID())
