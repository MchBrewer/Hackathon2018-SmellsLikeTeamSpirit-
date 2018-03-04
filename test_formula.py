from formula import Formula

formulaType = "sigma"
parameters = {"_i_":0, "_n_":10, "_result_":"0"}
variableNames = {"_i_":"i", "_n_":"n", "_k_":"k", "_result_":"result"}
myFormula = Formula(formulaType, parameters, variableNames)
myFormula.printCode()
