class Radio:
    
    color = "Black"
    brand = "Sony"
    ACPower = "yes"
    headphone = "no"
    
    def __init__(self):
        self.power_led = "ON"
        self.mode_led = "OFF"
        self.frequency = 0.0
        self.volume = 0
        print("Welcome to Sony Radio!")
        
    def power_switch(self,power):
        self.power_led = power
        print("Power is ", self.power_led)
        
    def mode_switch(self, mode):
        self.mode_led = mode
        print("Mode is ", self.mode_led)
        
    def band_tuner(self, band):
        self.frequency = band
        print("Frequency = ", self.frequency)
        
    def volume_tumer(self, fmvolume):
        self.volume = fmvolume
        print("Volume = ", self.volume)
        
radio_sample = Radio()
print("color of radio = ", Radio.color)
print("Brand = ", Radio.brand)
print("AC Power source = ", Radio.ACPower)
print("Headphone Jack Availability = ", Radio.headphone)

radio_sample.power_switch("ON")
radio_sample.mode_switch("FM")
radio_sample.band_tuner(102.2)
radio_sample.volume_tumer(8)
radio_sample.power_switch("OFF")
radio_sample = None