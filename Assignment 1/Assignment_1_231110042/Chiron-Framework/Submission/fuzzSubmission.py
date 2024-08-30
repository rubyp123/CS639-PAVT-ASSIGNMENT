from kast import kachuaAST
import sys
import random
import copy
from z3 import *
sys.path.insert(0, "KachuaCore/interfaces/")
from interfaces.fuzzerInterface import *
sys.path.insert(0, '../KachuaCore/')

# Each input is of this type.
#class InputObject():
#    def __init__(self, data):
#        self.id = str(uuid.uuid4())
#        self.data = data
#        # Flag to check if ever picked
#        # for mutation or not.
#        self.pickedOnce = False
        
class CustomCoverageMetric(CoverageMetricBase):
    # Statements covered is used for
    # coverage information.
    def __init__(self):
        super().__init__()

    # TODO : Implement this
    def compareCoverage(self, curr_metric, total_metric):
        # must compare curr_metric and total_metric
        # True if Improved Coverage else False
        if len(curr_metric) > len(total_metric):
            return True  # Improved coverage
        else:
            return False

    # TODO : Implement this
    def updateTotalCoverage(self, curr_metric, total_metric):
        # Compute the total_metric coverage and return it (list)
        # this changes if new coverage is seen for a
        # given input.
        total_metric.extend(curr_metric)  # Merge coverage information
        return list(set(total_metric))

class CustomMutator(MutatorBase):
    def __init__(self):
        pass


    # TODO : Implement this
    def mutate(self, input_data, coverageInfo, irList):
        # Mutate the input data and return it
        # coverageInfo is of type CoverageMetricBase
        # Don't mutate coverageInfo
        # irList : List of IR Statments (Don't Modify)
        # input_data.data -> type dict() with {key : variable(str), value : int}
        # must return input_data after mutation.
        mutated_data = copy.deepcopy(input_data)
        #print("--------------------------------",type(mutated_data.data))
        for i in mutated_data.data.keys():
            random_number = random.randint(0,2)
            if(random_number==0):
                num = random.randint(-128,128)
                mutated_data.data[i] = (mutated_data.data[i])^num
            if(random_number==1):
                num = random.randint(-128,128)
                mutated_data.data[i] = (mutated_data.data[i]) << 1
            if(random_number==2):
                num = random.randint(-128,128)
                mutated_data.data[i]= (mutated_data.data[i]) >> 1
                
        input_data = mutated_data
        return input_data
            

       


# Reuse code and imports from
# earlier submissions (if any).
