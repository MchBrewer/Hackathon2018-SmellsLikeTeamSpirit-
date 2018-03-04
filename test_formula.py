from formula import Formula

formulaType = "pi"
parameters = {"_i_":0, "_n_":99, "_function_":"lambda k: k"}
variableNames = {"_i_":"i", "_n_":"n", "_function_":"function", "_k_":"k", "_result_":"result"}
myFormula = Formula(formulaType, parameters, variableNames)
myFormula.printCode()
