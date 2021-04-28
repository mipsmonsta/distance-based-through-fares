from enum import Enum
from typing import Optional, List

class ServiceType(Enum):
    FEEDER = 1
    TRUNK = 2
    EXPRESS = 3

class Trip:
    def __init__(self, distance: float, svcType: ServiceType, start=None, end=None):
        self.distance = distance
        self.type = svcType

class AdultJourney:
    cardTrunkCurve = [92, 92, 92, 102, 112, 122, 131, 138, 144, 148, 152, 156, \
                160, 164, 168, 172, 176, 180, 184, 187, 190, 193, 196, \
                198, 200, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, \
                212, 213, 214, 215, 216, 217]


    cardExpressSurcharge = 60

    #cardFeederCurve = [92, 92, 92]

    def __init__(self, trips: Optional[List[Trip]]=None):
        self.trips = trips

    def addTrips(self, trip: Trip):
        if self.trips == None:
            self.trips = [trip]
        else:
            self.trips.append(trip)
    
    def calculateFares(self, debug=False):
        totalDistance = 0
        beforeSurcharge = 0
        numexpressTaken = 0
        for trip in self.trips:
            if trip.type == ServiceType.FEEDER:
                totalDistance += trip.distance if trip.distance < 3.2 else 3.2
            else:
                totalDistance += trip.distance
            if trip.type == ServiceType.EXPRESS:
                numexpressTaken += 1

        if totalDistance > 40.2:
            beforeSurcharge = AdultJourney.cardTrunkCurve[-1]
        
        for i in range(len(AdultJourney.cardTrunkCurve)):
            if totalDistance <= (i+1.2):
                beforeSurcharge = AdultJourney.cardTrunkCurve[i]
                break
        
        if debug:
            print(totalDistance)

        return beforeSurcharge + AdultJourney.cardExpressSurcharge * numexpressTaken

if __name__ == '__main__':
    aj = AdultJourney()
    trip1 = Trip(4.2, svcType=ServiceType.FEEDER)
    trip2 = Trip(6.2, svcType=ServiceType.EXPRESS)

    aj.addTrips(trip1)
    aj.addTrips(trip2)

    print(aj.calculateFares(debug=True))

    
        

