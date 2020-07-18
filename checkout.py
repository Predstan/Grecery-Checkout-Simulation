# Implementation of Buyer and checkpoint ADT for Grocery checkpoint Simulation

from Array import Array
from Queue import queue
from random import randint

class Buyer:
    # Creates an instance of the a Buyer
    def __init__( self, idNum, arrivalTime ):
        self._idNum = idNum
        self._arrivalTime = arrivalTime

    # Return the id Number given to a buyer
    def idNum( self ):
        return self._idNum

    # Return the Arrival Time of a Buyer
    def arrivalTime( self ):
        return self._arrivalTime



class checkpoint:
    # Creates an instance of a single Chcekpoint
    def __init__( self, idNum ):
        self._idNum = idNum
        self._buyer = None
        self._stoptime = -1

    # Return the id number of the checkpoint
    def idNum ( self ):
        return self._idNum

    # Determine if Chcekpoint is Free
    def isFree( self ):
        return self._buyer is None

    # Determine if a checkpoint in use us now free
    def isFinished( self, stoptime ):
        return self._buyer is not None and stoptime == self._stoptime

    # Checkout a buyer
    def checkout( self, buyer, stoptime ):
        self._buyer = buyer
        self._stoptime = stoptime

    # End checkout
    def endcheckout( self ):
        thebuyer = self._buyer
        self._buyer = None
        return thebuyer


class checkoutLine:
    # Create an instance of the Chcekout Line
    def __init__( self, idNum, numCheckPoint ):
        self._idNum = idNum
        self._numCheckPoint = numCheckPoint
        self._point = 0
        self._checkPoints = Array( numCheckPoint )
        self._lineQueue = queue()
        self._check = 0

        # Create the number of checkpoint
        for i in range( numCheckPoint ):
            self._checkPoints[i] = checkpoint( 0+1 )

    # Return the id number of a checkLine
    def idNum(self):
        return self._idNum

    # Return the number of chcekpoint in the Line
    def numCheckPoint( self ):
        return self._numCheckPoint

    # Determine if a line is available
    def isAvailable( self ):
        return self._point != self._numCheckPoint

    # Return the number of checkpoint in use in a Line
    def numInUse( self ):
        return self._point
    
    # Accept the arrival of a buyer in Line Queue
    def arrive( self, buyer, curTime ):
        self._lineQueue.enqueue(buyer)
        print( " Time {} : Buyer {} arrived at Line {}"\
                    .format(curTime, buyer.idNum(), self.idNum()))

    # Buyer checkout in a line according to arrival
    def checkout( self, curTime, minCheckTime, maxCheckTime):
        i = 0
        self._check = 0
        waitTime = 0

        while i < self._numCheckPoint:
            if self._checkPoints[i].isFree() and not self._lineQueue.isEmpty():
                serviceTime = randint(minCheckTime, maxCheckTime)
                stopTime = curTime + serviceTime
                buyer = self._lineQueue.dequeue()
                self._checkPoints[i].checkout( buyer, stopTime)
                self._point += 1
                self._check += 1
                waitTime += curTime - buyer.arrivalTime()
                print( " Time {} : Buyer {} started Check Out at Line {}, checkpoint {}"\
                    .format(curTime, buyer.idNum(), self.idNum(), i+1))
            i += 1

        return waitTime

    # Buyer ended checkout
    def endCheckout( self, stoptime ):
        i = 0

        while i < self._numCheckPoint:
            if self._checkPoints[i].isFinished(stoptime):
                buyer = self._checkPoints[i].endcheckout()
                self._point -= 1
                print( " Time {} : Buyer {} ended at Line {}, checkpoint {}"\
                    .format(stoptime, buyer.idNum(), self.idNum(), i+1 ))
            i += 1

    # return the number of checkout at a time
    def numcheck ( self):
        return self._check

    # Return the queue in a Line
    def lineQueue(self):
        return self._lineQueue

    # Buyer leaves Checkout line whithout checkout
    def leaveLine(self):
        buyer = self._lineQueue.dequeue()
        return buyer

        



    
        
    
    
        
        










