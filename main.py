def right(degrees: number):
    kitronik_servo_lite.turn_right(degrees)
def left(degrees: number):
    kitronik_servo_lite.turn_left(degrees)

def on_button_pressed_a():
    basic.show_string("F")
    kitronik_servo_lite.set_distance_per_second(200)
    left(90)
    forwards(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_free_fall():
    basic.show_string("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
input.on_gesture(Gesture.FREE_FALL, on_gesture_free_fall)

def backwords(distance: number):
    if distance == 0:
        kitronik_servo_lite.backward()
    else:
        kitronik_servo_lite.drive_backwards(distance)

def on_button_pressed_ab():
    kitronik_servo_lite.neutral()
    kitronik_servo_lite.stop()
    basic.show_string("STOPPED!")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("B")
    backwords(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def forwards(distance: number):
    if distance == 0:
        kitronik_servo_lite.forward()
    else:
        kitronik_servo_lite.drive_forwards(distance)
Pixel_Array = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB_RGB)
Pixel_Array.set_brightness(99)
Pixel_Array.show_rainbow(0, 255)
led.set_brightness(255)
kitronik_servo_lite.set_distance_per_second(200)
# forwards(300)
# basic.pause(1000)
# basic.show_icon(IconNames.HEART)
# basic.pause(1000)

def on_forever():
    basic.show_string(control.device_name())
basic.forever(on_forever)
