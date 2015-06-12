from crop_class import *
class Potato(crop):
    """A potato crop"""
    def __init__(self):
        #growth rate = 1; light need = 3; water need = 6
        super().__init__(1,3,6)
        self._type = "Potato"
def main():
    potato_crop = Potato()
    print(potato_crop.report())
    manual_grow(Potato_crop)
    print(potato_crop.report())

if __name__ == "__main__":
    main()
