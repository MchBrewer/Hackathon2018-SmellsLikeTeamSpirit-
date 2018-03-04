import re

class MarkdownError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, "Invalid markdown expression.")

class Formula(object):
    def __init__(self, formulaType, parameters, variableNames, markdown):
        self.formulaType = formulaType
        self.parameters = parameters
        self.variableNames = variableNames
        self.lambdaFunction = self.getLambdaFunctionFrom(markdown)
        self.parameters["_function_"] = self.lambdaFunction
        self.code = self.getCodeFor(formulaType, parameters)
    
    def getLambdaFunctionFrom(self, markdown):
        converted_markdown = self.convertSquareRootsIn(markdown)
        converted_markdown = converted_markdown.replace(self.variableNames["_k_"], "_k_")
        return converted_markdown
    
    def convertSquareRootsIn(self, markdown):
        phrase = "sqrt"
        converted_markdown = markdown
        while (converted_markdown.find(phrase) > -1):
            index = converted_markdown.find(phrase)
            open_parenthesis_index = index + len(phrase)
            closed_parenthesis_index = self.findCorrespondingClosedParenthesisFor(open_parenthesis_index, converted_markdown)
            converted_markdown = converted_markdown[:index] + \
                                 converted_markdown[open_parenthesis_index:closed_parenthesis_index+1] + \
                                 "**0.5" + \
                                 converted_markdown[closed_parenthesis_index+1:]
        return converted_markdown
    
    def findCorrespondingClosedParenthesisFor(self, indexOpenParenthesis, string):
        value = 0
        closed_parenthesis_index = indexOpenParenthesis
        for character_index in xrange(indexOpenParenthesis, len(string)):
            if string[character_index] == "(":
                value += 1
            elif string[character_index] == ")":
                value -= 1
                    
            # value will equal zero when the index of the corresponding closed
            # parenthesis is found
            if value == 0:
                return character_index
    
    def getCodeFor(self, formulaType, parameters):
        if formulaType == "sigma":
            with open('formula_sigma_notation.txt', 'r') as file:
                code = file.read()
                for parameter, value in parameters.items():
                    code = code.replace(parameter + " = None", parameter + " = " + str(value))
                return code
        elif formulaType == "pi":
            with open('formula_pi_notation.txt', 'r') as file:
                code = file.read()
                for parameter, value in parameters.items():
                    code = code.replace(parameter + " = None", parameter + " = " + str(value))
                return code
        elif formulaType == "permutation":
            with open('formula_pi_notation.txt', 'r') as file:
                code = file.read()
                for parameter, value in parameters.items():
                    code = code.replace(parameter + " = None", parameter + " = " + str(value))
                return code
        elif formulaType == "combination":
            with open('formula_pi_notation.txt', 'r') as file:
                code = file.read()
                for parameter, value in parameters.items():
                    code = code.replace(parameter + " = None", parameter + " = " + str(value))
                return code
        
    
    def changeParameterNames(self, parameters):
        for old_name, new_name in parameters.items():
            self.code = self.code.replace(old_name, new_name)
            
    def getCode(self):
        return self.code
