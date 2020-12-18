input.onButtonPressed(Button.A, function () {
    basic.showString("F")
    kitronik_servo_lite.setDistancePerSecond(200)
    kitronik_servo_lite.forward()
})
input.onButtonPressed(Button.B, function () {
    basic.showString("B")
    kitronik_servo_lite.setDistancePerSecond(200)
    kitronik_servo_lite.backward()
})
let Pixel_Array = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB_RGB)
Pixel_Array.setBrightness(1000)
Pixel_Array.showRainbow(0, 255)
led.setBrightness(255)
basic.forever(function () {
	
})
