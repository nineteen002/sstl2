class LexicalAnalyzer:

    def __init__(self):
        self.tokens = {
            'for' : 'Palabra Reservada (Ciclo For)',
            'while' : 'Palabra Reservada (Ciclo While)',

            'if' : 'Palabra Reservada (Condicional If)',
            'else' : 'Palabra Reservada (Condicional Else)',
            'switch' : 'Palabra Reservada (Condicional Switch)',

            '+' : 'Operador Aritmetico (Suma)',
            '-' : 'Operador Aritmetico (Resta)',
            '/' : 'Operador Aritmetico (Division)',
            '*' : 'Operador Aritmetico (Multiplicacion)',

            '||' : 'Operador Logico (Or)',
            '&&' : 'Operador Logico (And)',

            '==' : 'Operador Relacional (Igual a)',
            '!=' : 'Operador Relacional (Diferente a)',
            '<' : 'Operador Relacional (Menor a)',
            '>' : 'Operador Relacional (Mayor a)',
            '<=' : 'Operador Relacional (Menor o igual a)',
            '>=' : 'Operador Relacional (Mayor o igual a)',

            'int' : 'Tipo de Dato (Entero)',
            'float' : 'Tipo de Dato (Punto Flotante)',
            'double' : 'Tipo de Dato (Double)',
            'bool' : 'Tipo de Dato (Booleano)',
            'char' : 'Tipo de Dato (Char)',

            'True' : 'Valor Booleano (True)',
            'False' : 'Valor Booleano (False)',

            'case' : 'Palabra Reservada (Case)',
            'break' : 'Palabra Reservada (Break)',

            'class' : 'Palabra Reservada (Clase)',
            'struct' : 'Palabra Reservada (Struct)',

            'void' : 'Palabra Reservada (Void)',
            'return' : 'Palabra Reservada (Return)',

            'const' : 'Palabra Reservada (Const)',
            'enum' : 'Palabra Reservada (Enum)',
            
            ';' : 'Simbolo del Lenguaje (Punto y Coma)'
            }

    def recognize(self, words):
        words = str(words).split()
        number_words = len(words)
        category = ""

        for word in words:
            if word in self.tokens:
                category += self.tokens[word]
            elif word.isnumeric():
                category += "Numero es '" + word + "' con " + str(len(word)) + " digitos"
            else:
                category += "Palabra NO reservada: '" + word + "' de " + str(len(word)) + " caracteres"
            if number_words > 1:
                category += ", "
                number_words -= 1

        return category

    def user_interface(self):
        exit = 0
        while not exit:
            word = input("Ingrese una palabra: ")
            print(self.recognize(word))

            exiting = input("Desea salir? [Y/N]: ")
            if exiting == 'Y' or exiting == 'y':
                exit = 1


if __name__ == '__main__':
    analyzer = LexicalAnalyzer()
    analyzer.user_interface()