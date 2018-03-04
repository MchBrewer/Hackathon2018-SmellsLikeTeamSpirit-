import os

class Formula(object):
    def __init__(self, formulaType, parameters):
        self.formulaType = formulaType
        self.parameters = parameters
        self.code = self.getCodeFor(formulaType, parameters)
        
    def getCodeFor(self, formulaType, parameters):
        if formulaType == "sigma":
            with open('formula_sigma_notation.txt', 'r') as file:
                code = file.read()
                for parameter, value in parameters.items():
                    code = code.replace(parameter + " = 0", parameter + " = " + str(value))
                return code
        if formulaType == "pi":
            with open('formula_pi_notation.txt', 'r') as file:
                code = file.read()
                for parameter, value in parameters.items():
                    code = code.replace(parameter + " = 0", parameter + " = " + str(value))
                return code
    
    def printCode(self):
        print self.code
        
print os.getcwd()

formulaType = "pi"
parameters = {"_i_":0, "_n_":10, "_function_":"lambda k: k"}
myFormula = Formula(formulaType, parameters)
myFormula.printCode()