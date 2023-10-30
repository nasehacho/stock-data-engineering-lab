
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
        
        averages = []
        for row in self.data:
            new_stock_prices=row[1:]
            y = []
            for x in new_stock_prices:
                try:
                    y.append(float(x.strip()))
            
                except ValueError:
                    continue
            average = stats.mean(y)
            rounded_average = round(average,3)
            averages.append(rounded_average)
        return averages
        
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