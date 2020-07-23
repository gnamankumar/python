
class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention")
        print("Compiling")
        print("Running")



class Lapotop:

    def code(self,ide):
        ide.execute()

ide = MyEditor()

lap1 = Lapotop()
lap1.code(ide)
