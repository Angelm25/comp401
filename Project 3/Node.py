
class Node:
    Value = ""
    child = []

    def __init__(self, Value, Dict):
        self.SetValue(Value)
        self.Create_Child(Dict)

    def __str__(self):
        return str(self.Value)
    
    def SetValue(self, Value):
        self.Value = Value
        
    def Create_Child(self, Dict):
        if(isinstance(Dict, dict)):
            self.children = Dict.keys()


if __name__ == '__main__':
    main()

