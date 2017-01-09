from superman import *

jimmy_olsen = Sidekick("Jimmy Olsen")

superman = Superman()
superman.sidekicks.add(jimmy_olsen)
# superman.add_power("")
superman.fly()
print(superman)
# print(dir(superman))