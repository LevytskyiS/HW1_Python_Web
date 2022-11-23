class Meta(type):

    class_number = 0
    
    def __init__(cls, name, base, attrs):
        super().__init__(name, base, attrs)
        cls.class_number = Meta.class_number
        Meta.class_number += 1


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)