class Employee:
    def work(self):
        print("Employee working")

class Manager(Employee):
    def manage(self):
        print("Managing team")

m = Manager()
m.work()
m.manage()
