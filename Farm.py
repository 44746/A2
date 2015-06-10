class Crop:
    """"A generic food crop"""

    def __init__(self,growth_rate,light_need,water_need):
        self._growth_rate = 0
        self._days_growing= 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

    def need(self):
        return {'light need':self._light_need,'water need':self._water_need}
    def report(self):
        return {'type':self._type,'status':self._status,'growt':self._growth_rate,'days growing':self._days_growing}
def main():
    new_crop = Crop(1,4,3)
    print(new_crop.need())
    print(new_crop.report())
    
if __name__ == "__main__":
    main()
