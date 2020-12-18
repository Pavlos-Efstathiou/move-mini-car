def on_button_pressed_a():
    basic.show_string("F")
    kitronik_servo_lite.set_distance_per_second(200)
    kitronik_servo_lite.forward()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("B")
    kitronik_servo_lite.set_distance_per_second(200)
    kitronik_servo_lite.backward()
input.on_button_pressed(Button.B, on_button_pressed_b)

Pixel_Array = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB_RGB)

def on_forever():
    Pixel_Array.set_brightness(1000)
    Pixel_Array.show_rainbow(0, 255)
    basic.pause(2000)
    basic.show_string("" + str((Pixel_Array.power())))
    basic.pause(2000)
basic.forever(on_forever)
