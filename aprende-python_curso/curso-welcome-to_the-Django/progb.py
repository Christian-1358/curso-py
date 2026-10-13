print('Begin',__name__)
import proga

print("Difine fB")
def fB():
    print("dentro fB")
    proga.fA()
print("chama fB")
fB()

print('end', __name__)