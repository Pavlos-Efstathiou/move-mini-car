input.onButtonPressed(Button.A, function () {
    kitronik_servo_lite.setDistancePerSecond(200)
    kitronik_servo_lite.forward()
})
let Pixel_Array = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB_RGB)
basic.forever(function () {
    Pixel_Array.showRainbow(1, 255)
    basic.pause(2000)
    Pixel_Array.shift(4)
})
