from gpiozero import Button, LED
import time

LED_PIN = 12
BUTTON_PIN = 27
led = LED(LED_PIN)
button = Button(BUTTON_PIN)

def button_callback():
    print("Button pressed")
    led.on()

def main():
    button.when_pressed = button_callback
    print("Waiting for button")
    button.wait_for_press()

if __name__ == '__main__':
    main()
