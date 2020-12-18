function right (degrees: number) {
    kitronik_servo_lite.turnRight(degrees)
}
function left (degrees: number) {
    kitronik_servo_lite.turnLeft(degrees)
}
input.onButtonPressed(Button.A, function () {
    basic.showString("F")
    kitronik_servo_lite.setDistancePerSecond(200)
    left(90)
    forwards(0)
})
input.onGesture(Gesture.FreeFall, function () {
    basic.showString("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
})
function backwords (distance: number) {
    if (distance == 0) {
        kitronik_servo_lite.backward()
    } else {
        kitronik_servo_lite.driveBackwards(distance)
    }
}
input.onButtonPressed(Button.B, function () {
    basic.showString("B")
    kitronik_servo_lite.setDistancePerSecond(200)
    backwords(0)
})
function forwards (distance: number) {
    if (distance == 0) {
        kitronik_servo_lite.forward()
    } else {
        kitronik_servo_lite.driveForwards(distance)
    }
}
let Brightness_Value = led.brightness()
let Pixel_Array = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB_RGB)
Pixel_Array.setBrightness(1000)
Pixel_Array.showRainbow(0, 255)
led.setBrightness(255)
left(90)
forwards(0)
right(90)
forwards(0)
// forwards(300)
// basic.pause(1000)
// basic.show_icon(IconNames.HEART)
// basic.pause(1000)
basic.forever(function () {
	
})
