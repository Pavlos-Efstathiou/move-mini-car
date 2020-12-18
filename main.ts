input.onButtonPressed(Button.A, function () {
    pins.servoWritePin(AnalogPin.P1, 90)
    pins.servoWritePin(AnalogPin.P2, 90)
})
let Pixel_Array = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB_RGB)
basic.forever(function () {
    Pixel_Array.showRainbow(1, 360)
    basic.pause(2000)
})
