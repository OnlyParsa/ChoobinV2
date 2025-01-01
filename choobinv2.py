import re


class ChoobinInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.classes = {}
        self.modules = {}

    def evaluate(self, expression, local_vars={}):
        try:
            if isinstance(expression, str):
                if expression.startswith('"') and expression.endswith('"'):
                    return expression[1:-1]  # Handle string literals
                if expression in local_vars:
                    return local_vars[expression]  # Local variable
                if expression in self.variables:
                    return self.variables[expression]  # Global variable
            return eval(expression, {}, {**self.variables, **local_vars})  # Evaluate mathematical expressions
        except Exception as e:
            raise ValueError(f"Error evaluating expression: {expression} ({e})")

    def execute_say(self, command, local_vars):
        match = re.match(r'say\s+(.+)', command)
        if match:
            value = self.evaluate(match.group(1), local_vars)
            print(value)
        else:
            raise SyntaxError(f"Invalid syntax in 'say': {command}")

    def execute_set(self, command, local_vars):
        match = re.match(r'set\s+(\w+)\s*=\s*(.+)', command)
        if match:
            var_name = match.group(1)
            value = self.evaluate(match.group(2), local_vars)
            self.variables[var_name] = value
        else:
            raise SyntaxError(f"Invalid syntax in 'set': {command}")

    def execute_repeat(self, command, local_vars):
        match = re.match(r'repeat\s+(\d+)\s*\{\s*(.+)\s*\}', command)
        if match:
            count = int(match.group(1))
            body = match.group(2)
            for _ in range(count):
                self.interpret(body, local_vars)
        else:
            raise SyntaxError(f"Invalid syntax in 'repeat': {command}")

    def execute_for(self, command, local_vars):
        match = re.match(r'for\s+(\w+)\s+in\s+range\((.+)\)\s*\{\s*(.+)\s*\}', command)
        if match:
            var_name = match.group(1)
            range_expr = match.group(2)
            body = match.group(3)
            start, end = map(int, range_expr.split(','))
            for i in range(start, end):
                local_vars[var_name] = i
                self.interpret(body, local_vars)
        else:
            raise SyntaxError(f"Invalid syntax in 'for': {command}")

    def execute_while(self, command, local_vars):
        match = re.match(r'while\s+\((.+)\)\s*\{\s*(.+)\s*\}', command)
        if match:
            condition = match.group(1)
            body = match.group(2)
            while self.evaluate(condition, local_vars):
                self.interpret(body, local_vars)
        else:
            raise SyntaxError(f"Invalid syntax in 'while': {command}")

    def execute_if(self, command, local_vars):
        match = re.match(r'if\s+\((.+)\)\s*\{\s*(.+)\s*\}\s*(else\s*\{\s*(.+)\s*\})?', command)
        if match:
            condition = self.evaluate(match.group(1), local_vars)
            if condition:
                self.interpret(match.group(2), local_vars)
            elif match.group(4):
                self.interpret(match.group(4), local_vars)
        else:
            raise SyntaxError(f"Invalid syntax in 'if': {command}")

    def execute_def(self, command):
        match = re.match(r'def\s+(\w+)\((.*?)\)\s*\{\s*(.+)\s*\}', command)
        if match:
            func_name = match.group(1)
            params = match.group(2).split(',')
            body = match.group(3)
            self.functions[func_name] = (params, body)
        else:
            raise SyntaxError(f"Invalid syntax in 'def': {command}")

    def execute_call(self, command, local_vars):
        match = re.match(r'(\w+)\((.*?)\)', command)
        if match:
            func_name = match.group(1)
            args = match.group(2).split(',')
            if func_name in self.functions:
                params, body = self.functions[func_name]
                if len(params) != len(args):
                    raise ValueError(f"Function {func_name} expects {len(params)} arguments, got {len(args)}")
                local_vars = {param.strip(): self.evaluate(arg.strip(), local_vars) for param, arg in zip(params, args)}
                self.interpret(body, local_vars)
            else:
                raise NameError(f"Function {func_name} is not defined")
        else:
            raise SyntaxError(f"Invalid syntax in function call: {command}")

    def execute_class(self, command):
        match = re.match(r'class\s+(\w+)\s*\{\s*(.+)\}', command)
        if match:
            class_name = match.group(1)
            body = match.group(2)
            self.classes[class_name] = body
        else:
            raise SyntaxError(f"Invalid syntax in 'class': {command}")

    def execute_new(self, command, local_vars):
        match = re.match(r'new\s+(\w+)\((.*?)\)', command)
        if match:
            class_name = match.group(1)
            args = match.group(2).split(',')
            if class_name in self.classes:
                body = self.classes[class_name]
                local_vars = {f"self.{param.strip()}": self.evaluate(arg.strip(), local_vars) for param, arg in zip(args, args)}
                self.interpret(body, local_vars)
            else:
                raise NameError(f"Class {class_name} is not defined")
        else:
            raise SyntaxError(f"Invalid syntax in 'new': {command}")

    def execute_try(self, command, local_vars):
        match = re.match(r'try\s*\{\s*(.+)\s*\}\s*except\s*\{\s*(.+)\s*\}', command)
        if match:
            try_body = match.group(1)
            except_body = match.group(2)
            try:
                self.interpret(try_body, local_vars)
            except Exception as e:
                self.interpret(except_body, local_vars)
        else:
            raise SyntaxError(f"Invalid syntax in 'try-except': {command}")

    def execute_import(self, command):
        match = re.match(r'import\s+(\w+)', command)
        if match:
            module_name = match.group(1)
            try:
                module = __import__(module_name)
                self.modules[module_name] = module
            except ImportError:
                raise ImportError(f"Module {module_name} not found")
        else:
            raise SyntaxError(f"Invalid syntax in 'import': {command}")

    def interpret(self, line, local_vars={}):
        line = line.strip()
        if line.startswith("say"):
            self.execute_say(line, local_vars)
        elif line.startswith("set"):
            self.execute_set(line, local_vars)
        elif line.startswith("repeat"):
            self.execute_repeat(line, local_vars)
        elif line.startswith("for"):
            self.execute_for(line, local_vars)
        elif line.startswith("while"):
            self.execute_while(line, local_vars)
        elif line.startswith("if"):
            self.execute_if(line, local_vars)
        elif line.startswith("def"):
            self.execute_def(line)
        elif line.startswith("class"):
            self.execute_class(line)
        elif line.startswith("new"):
            self.execute_new(line, local_vars)
        elif line.startswith("try"):
            self.execute_try(line, local_vars)
        elif line.startswith("import"):
            self.execute_import(line)
        else:
            self.execute_call(line, local_vars)

    def run(self):
        print("Choobin Interpreter - Enter code:")
        while True:
            try:
                code = input(">>> ")
                if code.lower() == "exit":
                    break
                self.interpret(code)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    interpreter = ChoobinInterpreter()
    interpreter.run()
