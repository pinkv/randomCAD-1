import pifacecad as p
import pifacecad.tools as pifacetools
from time import sleep
import random
cad = p.PiFaceCAD()
cad.lcd.backlight_on()


while not cad.switches[4].value:
	cad.lcd.clear()
	cad.lcd.write("Random number")
	sleep(1)
	scanner = pifacetools.LCDScanf("from %3i > %3i%r", cad)
	randomRange = scanner.scan()
	
	while not cad.switches[1].value:
		number = random.randint(randomRange[0],randomRange[1])
		cad.lcd.set_cursor(0,1)
		cad.lcd.write(str(number))
		cad.lcd.write("                ")
		
		while not cad.switches[0].value:
			if cad.switches[4].value:
				break
			if cad.switches[1].value:
				break
			sleep(0.1)
		if cad.switches[4].value:
			break
		
