from main import mlops 

mlopsObj = mlops(5)

print("Testing main.py")
print("Runnign through script with jenkins")
def test_gettotalstudents(): assert mlopsObj.gettotalstudents() == 5

def test_Addstudent(): 
    mlopsObj.Addstudent()
    assert mlopsObj.gettotalstudents() == 6

def test_removeStudent():
    mlopsObj.removestudent()
    assert mlopsObj.gettotalstudents() == 5

def test_getclassname():
    assert mlopsObj.getclassname() == "MLOPS B"