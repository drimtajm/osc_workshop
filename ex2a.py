from gpiozero import Button, LED
import time

LED_PIN = 13
BUTTON_PIN = 27
led = LED(LED_PIN)
button = Button(BUTTON_PIN)

def button_callback():
    led.on()

def main():
    button.when_pressed = button_callback
    print("Waiting for button")
    button.wait_for_press()
    print("Button pressed")

if __name__ == '__main__':
    main()
