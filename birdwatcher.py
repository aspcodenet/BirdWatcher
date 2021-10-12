# Hålla reda på antal fåglar vi sett per dag
# de senaste 7 dagarna
# MAX 7 dagar
# aktuell dag är sist i listan
# incrementTodaysCount() - alltid på senaste i listan
# byta dag
#  [2, 5, 3, 7, 8, 6, 3]

class Birdwatcher:
    def __init__(self):
        #self._observationsPerDay = [0,0,0,0,0,0,0]
        self._observationsPerDay = [1,2,3,4,5,6,7]

    def hasDayWithoutBirds(self) -> bool:
        #return 0 in self._observationsPerDay
        for x in self._observationsPerDay:
            if x == 0:
                return True
        return False

    def setNewDay(self):
        for x in range(1,7):
            self._observationsPerDay[x-1] = self._observationsPerDay[x]
        self._observationsPerDay[6] = 0

    def incrementTodaysCount(self):
        lastIndex = len(self._observationsPerDay)-1
        self._observationsPerDay[lastIndex] = self._observationsPerDay[lastIndex] + 1
    
    def getCountToday(self) -> int:
        lastIndex = len(self._observationsPerDay)-1
        return self._observationsPerDay[lastIndex]

    def getCountThisWeek(self) -> int:
        sum = 0
        for x in self._observationsPerDay:
            sum  = sum + x
        return sum

