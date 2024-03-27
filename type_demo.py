from dataclasses import dataclass

@dataclass

class Snack:
    name: str  
    condiments: set[str]
    error_code: int 
    disposed_of: bool 
    
Snack("Hotdog", {"Mustard", "Ketchup"}, 5, False)

   