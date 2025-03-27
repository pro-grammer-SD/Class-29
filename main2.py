class Person(object):
    """docstring for Person."""
    def __init__(self):
        super(Person, self).__init__()
        
        self.name, self.id_ = None, None
        
class Employee(Person):
    """docstring for Employee."""
    def __init__(self, name: str, id_: int):
        super(Employee, self).__init__()
        
        self.name, self.id_ = name, id_
        
chatgpt = Employee("ChatGPT", 2024)
print(chatgpt.name, chatgpt.id_)