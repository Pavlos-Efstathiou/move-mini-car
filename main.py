def on_button_pressed_a():
    basic.show_string("F")
    kitronik_servo_lite.set_distance_per_second(200)
    kitronik_servo_lite.forward()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_free_fall():
    pass
input.on_gesture(Gesture.FREE_FALL, on_gesture_free_fall)

def on_button_pressed_ab():
    global Brightness_Value
    if Brightness_Value <= 255:
        Brightness_Value -= 50
    if Brightness_Value <= 120:
        Brightness_Value += 50
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("B")
    kitronik_servo_lite.set_distance_per_second(200)
    kitronik_servo_lite.backward()
input.on_button_pressed(Button.B, on_button_pressed_b)

Brightness_Value = 0
Brightness_Value = led.brightness()
Pixel_Array = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB_RGB)
Pixel_Array.set_brightness(1000)
Pixel_Array.show_rainbow(0, 255)
led.set_brightness(255)

def on_forever():
    pass
basic.forever(on_forever)
