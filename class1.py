
class Hello:
    def __init__(self,
                 name):
        self.name=name


class HI(Hello):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return self.name



