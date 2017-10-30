"""fulfills Ynon Perek's nontrivial python, Classes, part 1"""


class Widget(object):
    """widget that keeps track of dependences"""

    def __init__(self, name):
        """initializes object with a name and no dependencies"""
        self.name = name
        self.dependencies = []

    def addDependency(self, *args):
        """Adds object to the list of dependencies for this object
        Object must have getDependencies function"""
        self.dependencies = self.dependencies + list(args)

    def build(self):
        """prints complete build list"""
        buildList = self.getDependencies([])
        build = ', '.join(buildList[:-1])
        print(build)

    def getDependencies(self, buildList):
        """gets complete build list with no duplicates"""
        for character in self.dependencies:
            if character.name in buildList:
                continue
            buildList = character.getDependencies(buildList[:])
        return buildList + [self.name]


def main():
    luke = Widget("Luke")
    hansolo = Widget("Han Solo")
    leia = Widget("Leia")
    yoda = Widget("Yoda")
    padme = Widget("Padme Amidala")
    anakin = Widget("Anakin Skywalker")
    obi = Widget("Obi-Wan")
    darth = Widget("Darth Vader")
    _all = Widget("All")

    luke.addDependency(hansolo, leia, yoda)
    leia.addDependency(padme, anakin)
    obi.addDependency(yoda)
    darth.addDependency(anakin)

    _all.addDependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
    _all.build()
    # code should print: Han Solo, Padme Amidala, Anakin Skywalker,
    #                    Leia, Yoda, Luke, Obi-Wan, Darth Vader

if __name__ == '__main__':
    main()
