from typing import List

class Segment:
    def __init__(self,departure,destination):
        self.departure = departure
        self.destination = destination



class Flight:
    def __init__(self,segments: List[Segment]):
        self.segemets = segments

    def __repr__(self):
        return f'{self.departure_point} -> {" -> ".join([p.destination for p in self.segemets])}'

    @property
    def departure_point(self) -> str:
        return self.segemets[0].departure

    @departure_point.setter
    def departure_point(self,val):
        # self.segemets[0].departure = val
        dest = self.segemets[0].destination
        self.segemets[0] = Segment(val,dest)





flight = Flight([Segment('GLA','LHR'),Segment('LHR','EDN')])

print(flight.departure_point)
flight.departure_point = 'EDI'
print(flight.departure_point)

print(flight)

