from z3 import *
import argparse
import json
import sys

sys.path.insert(0, '../KachuaCore/')

from sExecutionInterface import *
import z3solver as zs
from irgen import *
from interpreter import *
import ast

def example(s):
    # To add symbolic variable x to solver
    s.addSymbVar('x')
    s.addSymbVar('y')
    # To add constraint in form of string
    s.addConstraint('Implies(x==5+y,x==5)')
    s.addConstraint('And(x==y,x>5)')
    # s.addConstraint('Implies(x==4,y==x+8')
    # To access solvers directly use s.s.<function of z3>()
    print("constraints added till now",s.s.assertions())
    # To assign z=x+y
    s.addAssignment('z','x+y')
    #print(s.assignSymbolicEncoding('z'))
    # To get any variable assigned
    print("variable assignment of z =",s.getVar('z'))



def checkEq(args,ir):

    file1 = open("../Submission/testData.json","r+")
    testData=json.loads(file1.read())
    file1.close()

    file2 = open("../Submission/testData1.json","r+")
    testData1=json.loads(file2.read())
    file2.close()

    s = zs.z3Solver()
    test_data = convertTestData(testData)
    test_data1 = convertTestData(testData1)


    #print(testData)
    #output = args.output
    #example(s)
    # TODO: write code to check equivalence
   

    # Create a dictionary with alphabet characters as keys

    q = Int('q')
    r = Int('r')
    s = Int('s')
    t = Int('t')
    u = Int('u')
    v = Int('v')
    w = Int('w')
    z= Int('z')
    x = Int('x')
    y = Int('y')
    c1 = Int('c1')
    c2 = Int('c2')
    c3 = Int('c3')
    c4 = Int('c4')
    c5 = Int('c5')
    c6 = Int('c6')
    c7 = Int('c7')
    c8 = Int('c8')
    c9 = Int('c9')
    c10 = Int('c10')

   
    #Fatch TestCases
    parameter= {}
    Symb1={}

    for key, value in testData1.items():
        parameter[key] = eval(str(value.get("params")))

    for key, value in testData1.items():
        Symb1[key] = eval(str(value.get("symbEnc")))

    input=[]
    for var in parameter:
        input.append(parameter[var])
    
    output=[]
    for var in Symb1:
        output.append(Symb1[var])
    
    #print(input)
    #print(output)

    input_eq=[]
    for i in input:
        list=[]
        for j ,k in i.items():
            list.append(eval(str(j + "==" + str(k) )))
        input_eq.append(list)

    #print(input_eq)

    output_eq=[]
    for i in output:
        list=[]
        for j ,k in i.items():
            list.append(eval(str(j + "==" + str(k) )))
        output_eq.append(list)
   
    #print(output_eq)
 
    
    # FOR TESTDATA.JSON P1
    constraints={}
    symb2={}
    for key, value in testData.items():
        constraints[key] = eval(str(value.get("constraints")))

    for key, value in testData.items():
        symb2[key] = eval(str(value.get("symbEnc")))

    #print(constraints)
    constraint = []
    for i in constraints:
        constraint.append(eval(str(constraints[i])))

    #print(constraint)

    hole_output= []
    for i in symb2:
        hole_output.append(eval(str(symb2[i])))

    #print((hole_output))

 
    and_input = []
    for i in input_eq:
        AND = True 
        for j in range(0,len(i)):
            AND = And(AND , i[j])
        and_input.append(AND)
    #print(and_input)

    And_cons=[] 
   
    A=True
    for i in constraint:
        for j in i:
            split_strings = j[0:len(j)].split(',')
            result_list = [s.strip() for s in split_strings]
            A=True
            for k in range(0,len(result_list)):
               A=And(A,eval(str(result_list[k])))
            And_cons.append(A)    

     
    s1 = Solver()
    s2 = Solver()
    #print(input_eq)
    #print(And_cons)

    for i in range(0,len(and_input)):
        for j in range(0,len(And_cons)):
            s1.reset()
            s1.add(and_input[i])
            s1.add(And_cons[j])
            if s1.check()==sat:
                for key1 , value1 in output[i].items():
                    for key2 , value2 in hole_output[j].items():
                        if (key1==key2):
                            s2.add(eval(str(value1 + "==" + value2)))
                  
       

    if s2.check()==sat:
        print("Values of constant parameters : ")
        print(s2.model())
    else:
        print('Not Satisfied')
    
    


if __name__ == '__main__':
    cmdparser = argparse.ArgumentParser(
        description='symbSubmission for assignment Program Synthesis using Symbolic Execution')
    cmdparser.add_argument('progfl')
    cmdparser.add_argument(
        '-b', '--bin', action='store_true', help='load binary IR')
    cmdparser.add_argument(
        '-e', '--output', default=list(), type=ast.literal_eval,
                               help="pass variables to kachua program in python dictionary format")
    args = cmdparser.parse_args()
    ir = loadIR(args.progfl)
    checkEq(args,ir)
    exit()
