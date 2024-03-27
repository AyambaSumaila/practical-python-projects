class Circle:
    pie=3.14
    def __init__(self, radius):
        self.radius=radius
        
    def circle_cum(self):
        value_cir_cum=2 * Circle.radius * self.radius
        return value_cir_cum
    
    def circle_area(self):
        area=Circle.pie * self.radius**2
        return area
    
    
circle=Circle(123)
circle2=Circle(12)

circle.circle_area()
circle2.circle_cum()