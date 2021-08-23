#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回表达式的值
# @param s string字符串 待计算的表达式
# @return int整型
#
class Solution:
    def solve(self , s ):
        # write code here
        num_stack=list()
        op_stack=list()
        cur_symbol=''
        for i in range(len(s)):
            if s[i].isnumeric():
                cur_symbol+=s[i]
                if i==len(s)-1:
                    num_stack.append(int(cur_symbol))
            else:
                if cur_symbol:
                    num_stack.append(int(cur_symbol))
                cur_symbol=''
                if not op_stack or s[i]=='(':
                    op_stack.append(s[i])
                else:
                    if s[i]==')':
                        while op_stack[-1]!='(':
                            num2=num_stack.pop()
                            num1=num_stack.pop()
                            op=op_stack.pop()
                            num_stack.append(self.operation(num1, num2, op))
                        op_stack.pop()
                    else:
                        flag=self.priority(s[i], op_stack[-1])
                        if flag:
                            op_stack.append(s[i])
                        else:
                            num2=num_stack.pop()
                            num1=num_stack.pop()
                            op=op_stack.pop()
                            num_stack.append(self.operation(num1, num2, op))
                            op_stack.append(s[i])
#             print(num_stack, op_stack)
        while op_stack:
            num2=num_stack.pop()
            num1=num_stack.pop()
            op=op_stack.pop()
            num_stack.append(self.operation(num1, num2, op))
        return num_stack.pop()
    
    def priority(self, op1, op2):
        if op1==op2:
            return False
        if op2=='(':
            return True
        if op1=='*' and (op2=='+' or op2=='-'):
            return True
        return False
    
    def operation(self, num1, num2, symbol):
        if symbol=='+':
            return num1+num2
        if symbol=='-':
            return num1-num2
        if symbol=='*':
            return num1*num2
          
          
# （1）规定运算符优先级（详见具体操作步骤）

# （2）对输入的字符逐一检验

# 　　（a）如果是数字字符：按位权转化为数值

# 　　（b）如果不是数字字符：将上一步的数值压栈

# 　　　　i 如果是'('或符号栈为空：将该字符压入符号栈

# 　　　　ii 如果是')'或'='：将符号栈中所有符号弹出，每弹出一个符号从数据栈拿出两个数字进行计算，计算结果压入数据栈，直到数据栈为空或栈顶元素为'('为止

# 　　　　iii 其他情况：比较当前元素与栈顶元素的优先级

# 　　　　　　(i) 如果当前元素优先级 > 栈顶元素优先级：将当前元素压入符号栈

# 　　　　　　(ii) 如果当前元素优先级 <= 栈顶元素优先级：符号栈弹出一个符号进行运算，直到当前元素优先级 > 栈顶元素优先级

# 运算符优先级
# (: 0

# +  -: 1

# *  /  %: 2

# ^: 3
