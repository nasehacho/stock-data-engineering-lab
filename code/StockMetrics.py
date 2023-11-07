
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        
        # Empty list where calculated averages will be stored 
        averages = []
        # Inital loop that acts on rows of data in self.data 
        for row in self.data:
            # Removes unwanted data (Date) in new list to perform statistical functions
            new_stock_prices=row[1:]
            # List where cleaned data will be stored 
            y = []
            # Nested loop that acts on elements in new_stock_prices
            for x in new_stock_prices:
                # Loop that converts all values in the list to floating point numbers, strips any blank space for statistical evaluation, and adds the cleaned data to the y list
                try:
                    y.append(float(x.strip()))
            
                except ValueError:
                    continue
            # Average statistic function from statistics module imported initially. 
            average = stats.mean(y)
            # Returns rounded averages to the third decimal place
            rounded_average = round(average,3)
            # Adds rounded average values the averages list 
            averages.append(rounded_average)
        # Returns rounded averages from averages list 
        return averages

    #Methods from def average01(self): repeated for def median02(self):
    def median02(self):
      
        medians = []
        for row in self.data:
            new_stock_prices=row[1:]
            m = []
            for n in new_stock_prices:
                try:
                    m.append(float(n.strip()))
            
                except ValueError:
                    continue
            if m:
                median = stats.median(m)
                medians.append(median)
        return medians

    #Methods from def average01(self): repeated for def stddev03(self):
    def stddev03(self):
        
        stddev = []
        for row in self.data:
            new_stock_prices=row[1:]
            s = []
            for d in new_stock_prices:
                try:
                    s.append(float(d.strip()))
            
                except ValueError:
                    continue
            new_sd = stats.stdev(s)
            rounded_sd = round(new_sd,3)
            stddev.append(rounded_sd)
        return stddev