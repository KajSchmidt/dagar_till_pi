from Adafruit_LED_Backpack import AlphaNum4

display = AlphaNum4.AlphaNum4()
display.begin()

def visa(text):
	display.clear()
	display.print_str(str(text))
	display.write_display()
	return;
