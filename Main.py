from Analysis import Constellations
from Analysis import InterpretiveReport
from Analysis import StructuralSummary
import cfg

def main(arr):
    '''ENTRY POINT FILE
    this method
    1. initializes main methods in other files
    2. fills global variables
    3. passes global variables to othe .main methods in other Analysis files
    4. 3+ Passes data to output
    '''
    CNTNR_SS = StructuralSummary.main(arr)
    CNTNR_C, arr = Constellations.main(CNTNR_SS)
    CNTNR_IR = InterpretiveReport.main(CNTNR_SS, CNTNR_C)
    cfg.main(CNTNR_SS, CNTNR_C,arr,CNTNR_IR)

