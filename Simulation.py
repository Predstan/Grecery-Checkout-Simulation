# Proper Simulation for Checkout
from Array import Array
from checkout import Buyer, checkoutLine
from random import randint
from Queue import queue


class checkoutSimulation:
    # Accept user imput and create and instance of the Simulation
    # Number of CheckoutLine, Point per Line, Time between Arrival of Buyer
    # Maximum checkout Time, Minimum Checkout Time
    # Number of Seconds for Simulation
    def __init__(self, numCheckoutLine, pointPerLine, timeBetween, maxCheckTime, minCheckTime, numSeconds):
        self._arriveprob = 1.0 / timeBetween
        self._numSeconds = numSeconds
        self._maxCheckTime = maxCheckTime
        self._minCheckTime = minCheckTime
        self._pointPerLine = pointPerLine

        # Create Chcekout Line according to user input
        self._checkOutLines = Array(numCheckoutLine)
        for i in range(numCheckoutLine):
            self._checkOutLines[i] = checkoutLine( i+1, pointPerLine)



        self._numBuyers = 0
        self._totalWaitTime = 0
        self._buyersCheckOuts = 0

    # Reun Simulation 
    def run( self ):
            for curTime in range ( self._numSeconds + 1 ):
                self.handleArrival  ( curTime )
                self.changeLine ( curTime )
                self.handleCheckout ( curTime )
                self.endCheckout ( curTime )
            
            self.printResult()

    # Print Result of Simulation
    def printResult(self):
            if self._buyersCheckOuts != 0:
                avgwait = self._totalWaitTime / self._buyersCheckOuts
            else:
                avgwait = 0
            print(" average wait time was : {}".format(avgwait))
            print(" number of Buyers is {}".format(self._numBuyers))
            print("Number of CheckoutLine is ", len(self._checkOutLines))
            print(" number of Checkpoint per Line is :", self._pointPerLine)
            print( " Number of Buyers that Checked out within Time is {}".format(self._buyersCheckOuts))
            
    # Handle the Arrival of each Buyer into a checkOut line of Choice
    def handleArrival(self, curTime):
            prob = randint(0.0, 1.0)
            # Probability that a buyer arrive at this time
            if prob >= 0.0 and prob <= self._arriveprob and self._numBuyers < 9000:
                line = randint (0, len(self._checkOutLines) - 1)
                buyer = Buyer(self._numBuyers + 1, curTime)
                self._checkOutLines[line].arrive(buyer, curTime)
                self._numBuyers += 1

    # Handle checkout in each Line of Checkout
    def handleCheckout( self, curTime ):

            for i in range(len(self._checkOutLines)):
                waitTime = self._checkOutLines[i].checkout(curTime, self._minCheckTime, self._maxCheckTime)
                self._totalWaitTime += waitTime
                self._buyersCheckOuts += self._checkOutLines[i].numcheck()
                


    # Buyer Change Line when queue on a line is much
    def changeLine ( self, curTime):
        # Iterate over each line for Lines 
        for i in range(len(self._checkOutLines)):
            done = 0
            thisLine = len(self._checkOutLines[i].lineQueue())
            buyers = self._numBuyers - self._buyersCheckOuts
            avg = buyers//len(self._checkOutLines)
            # Determine if queue is more that 2 plus the number of buyer in each queue
            if thisLine > avg + 2 and avg > 0:
                # Changes line as long as queue is long
                for j in range(thisLine - avg ):
                    if thisLine > avg+2 and avg > 0:
                        # Buyer determine which line to go to
                        line = randint (0, len(self._checkOutLines) - 1)
                        # Check if line is available
                        if self._checkOutLines[line].isAvailable() and line != i:
                            buyer = self._checkOutLines[i].leaveLine()
                            print ("Buyer {} changed from line {} to Line {}".format(buyer.idNum(), i+ 1, line + 1))
                            self._checkOutLines[line].arrive(buyer, curTime)
                            done += 1
                

    # End checkout in each Line of checkout
    def endCheckout( self, curTime ):
            for i in range(len(self._checkOutLines)):
                self._checkOutLines[i].endCheckout( curTime )


            
done = checkoutSimulation(2, 4, 3, 20, 1, 1440)
done.run()