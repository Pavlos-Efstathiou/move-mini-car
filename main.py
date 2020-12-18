def on_button_pressed_a():
    kitronik_servo_lite.forward()
input.on_button_pressed(Button.A, on_button_pressed_a)

Pixel_Array = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB_RGB)

def on_forever():
    Pixel_Array.show_rainbow(1, 360)
    basic.pause(2000)
    Pixel_Array.shift(1)
basic.forever(on_forever)
