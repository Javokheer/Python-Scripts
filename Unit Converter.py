class Converter:
    """Returns Converted measurements"""
    def __init__(self, num, unit):
        self.num = num
        self.unit = unit
        self.conversion_table = {
            'mm': {'cm': 0.1, 'm': 0.001, 'km': 0.000001, 'in': 0.03937, 'ft': 0.003281},
            'cm': {'cm': 1, 'mm': 10, 'm': 0.01, 'km': 0.00001, 'in': 0.3937, 'ft': 0.03281},
            'm': {'mm': 1000, 'cm': 100, 'km': 0.001, 'in': 39.37, 'ft': 3.281}
        }

    def inches(self):
        """:return  Converted inches data type: float"""
        return (self.num * self.conversion_table[self.unit]['in'])

    def centimeter(self):
        """:return  Converted centimeter data type: float"""
        return (self.num * self.conversion_table[self.unit]['cm'])

    def meter(self):
        """:return  Converted meter data type: float"""
        return (self.num * self.conversion_table[self.unit]['m'])


c = Converter(10, 'cm')
print(c.inches())
print(c.centimeter())
print(c.meter())