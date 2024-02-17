from class_coworker import coworker
from class_order import order
class coworkers:
    def __init__(self) -> None:
        self.coworkers_list = [
            coworker("Bob", order("Cappuccino"), 0.0), #default aside from cappucino
            coworker("Jeremy", order("", False, False, 0), 0.0),  ##black coffee
            coworker("Susan", order(), 0.0), 
            coworker("John", order(), 0.0), 
            coworker("Mary", order(), 0.0), 
            coworker("Romeo", order(), 0.0), 
            coworker("Juliet", order(), 0.0), 
        ]