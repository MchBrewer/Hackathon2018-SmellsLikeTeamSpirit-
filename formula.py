class Formula(object):
    def __init__(self, formulaType, parameters, variableNames):
        self.formulaType = formulaType
        self.parameters = parameters
        self.lambdaFunction = parameters["_function_"]
        self.code = self.getCodeFor(formulaType, parameters)
        self.changeParameterNames(variableNames)
    
    def getLambdaFunctionFrom(userInput):
        # TODO make this function an interpreter from the syntax used
        # to display the function and Python syntax
        pass
    
    def getCodeFor(self, formulaType, parameters):
        if formulaType == "sigma":
            with open('formula_sigma_notation.txt', 'r') as file:
                code = file.read()
                for parameter, value in parameters.items():
                    code = code.replace(parameter + " = None", parameter + " = " + str(value))
                return code
        if formulaType == "pi":
            with open('formula_pi_notation.txt', 'r') as file:
                code = file.read()
                for parameter, value in parameters.items():
                    code = code.replace(parameter + " = None", parameter + " = " + str(value))
                return code
    
    def changeParameterNames(self, parameters):
        for old_name, new_name in parameters.items():
            self.code = self.code.replace(old_name, new_name)
            
    def printCode(self):
        print self.code
