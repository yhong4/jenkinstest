import json
from sympy import *

from sympy.parsing.latex import parse_latex
from sympy.parsing.sympy_parser import parse_expr
from sympy.printing.latex import latex

class JsonSerializable(object):
    def toJson(self):
        return json.loads(json.dumps(self.__dict__))
            
class Results(JsonSerializable):
    
    def __init__(self, query, solutions, isSelectSubject = False, subject = 0, topic = 0, lang = "en"):
        self.query = query
        self.solutions = solutions
        self.isSelectSubject = isSelectSubject
        self.subject = subject
        self.topic = topic
        self.lang = lang
        
class Solution(JsonSerializable):
    
    def __init__(self, step_id, method, input_query, description, output_query, isDetails, details = []):
        self.step_id = step_id
        self.method = method
        self.input_query = input_query
        self.description = description
        self.output_query = output_query
        self.isDetails = isDetails
        self.details = details
        
class Detail(JsonSerializable):
    
    def __init__(self, detail_id, detail_method, detail_previous, detail_description, detail_after):
        self.detail_id = detail_id
        self.detail_method = detail_method
        self.detail_previous = detail_previous
        self.detail_description = detail_description
        self.detail_after = detail_after
        
class Term(JsonSerializable):
    
    def __init__(self, term_id, element, isColored = False, color = "", isCombine = False, isDescribed = False, description = ""):
        self.term_id = term_id
        self.element = element  # A latex string
        self.isColored = isColored
        self.color = color
        self.isCombine = isCombine
        self.isDescribed = isDescribed
        self.description = description


def element(expr):
    store = []
    if type(expr) == Add:
        for arg in expr.args:
            store += element(arg)
        return store
    else:
        return [expr]
    
def factor_example(expr):
    input_string = latex(expr)
    part1 = element(expr.args[0])
    part2 = element(expr.args[1])

    a = part1[0]
    b = part1[1]
    c = part2[0]
    d = part2[1]

    # solve:
    before = [Term(0, input_string).toJson()]
    after = [Term(0, latex(a) + "\cdot" +latex(c)).toJson(), Term(1, latex(a) + "\cdot" +latex(d)).toJson(), 
             Term(2, latex(b) + "\cdot" +latex(c)).toJson(), Term(3, latex(b) + "\cdot" +latex(d)).toJson()]

    step_id = 0
    method = "将括号里的多项式相乘并展开"

    description = ["套用展开运算法则", "(a-b)(c-d) = ac + ad + bc + bd"]

    isDetails = False

    solution1 = Solution(step_id, method, before, description, after, isDetails, details = [])

    results = Results(input_string, [solution1.toJson()])
    
    return results.toJson()

def handler(event, context):
    # TODO implement
    input_string = event["data"]["query"]
    expr = parse_latex(input_string)
    results = factor_example(expr)
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin" : "*",
            'Access-Control-Allow-Headers':'Access-Control-Allow-Origin,Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Content-Type': 'application/json'
          },
        "body": results
    }
