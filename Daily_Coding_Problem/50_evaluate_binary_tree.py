# Suppose an arithmetic expression is given as a binary tree. 
# Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

# Given the root to such a tree, write a function to evaluate it.
# x^y/(5*z)+2

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def precedence(char):
    if char == '+' or char == '-':
        return 1
    if char == '*' or char == '/':
        return 2


# k + l - m * n + (o * p) * w / u / v * t + q
def infixToPostfix(exp):
	stack = []
	postfix = ''
	for char in exp:
		if char == '(':
			stack.append(char)
		elif char.isalnum():
			postfix += char
		elif char == ')':
			while len(stack) > 0:
				top = stack.pop()
				if top == '(':
					break
				postfix += top
		else:
			if len(stack) == 0 or stack[-1] == '(' or precedence(char) > precedence(stack[-1]):
				stack.append(char)
			else:
				while len(stack) > 0 and stack[-1] != '(' and precedence(char) <= precedence(stack[-1]):
					top = stack.pop()
					postfix += top
				stack.append(char)
	while len(stack) > 0:
		postfix += stack.pop()
	return postfix


def createExpressionTree(exp):
    postfix = infixToPostfix(exp)
    stack = []
    for char in postfix:
        if char.isalnum():
            root = Node(char)
            stack.append(root)
        else:
            root = Node(char)
            right = stack.pop()
            left = stack.pop()
            root.left = left
            root.right = right
            stack.append(root)
    root = stack.pop()
    return root


def evaluateExpressionTree(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return int(root.val)
    left_sum = evaluateExpressionTree(root.left)
    right_sum = evaluateExpressionTree(root.right)
    if root.val == '+':
        return left_sum + right_sum
    elif root.val == '-':
        return left_sum - right_sum
    elif root.val == '*':
        return left_sum * right_sum
    elif root.val == '/':
        return left_sum / right_sum


def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)


expression = input('Enter a mathematical expression with no spaces and uses only +, -, *, / and (): ')
root = createExpressionTree(expression)
print(evaluateExpressionTree(root))