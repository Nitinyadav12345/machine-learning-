from logic import *
Symbol("rain") #it is raining
Symbol("hagrid") #harry visited hagrid
Symbol("dumbeldor") #harry visited dumbeldor
sentence = And(rain,hagrid)
print(sentence.formula())