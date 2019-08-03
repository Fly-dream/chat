import unittest

class TestSplitFunction(unittest.TestCase):
    registry = []  # Список-реестр «зарегистрированных» функций

    def register(func):
        ''' Декоратор, регистрирующий функции в неком "реестре" '''
        print(' running register ( %s ) ' % func)
        registry.append(func)
        return func

    # Функции, которые могут быть декорированы:
    @register
    def f1():
        print('running f1()')

    @register
    def f2():
        print('running f2()')

    # Намеренно декорируем не все функции
    def f3():
        print('running f3()')

    def main():
        print(' running main()')
        # Выведем список «зарегистрированных» функций
        print(' registry ->', registry)

        # Теперь просто выполним все функции
        f1()
        f2()
        f3()

    if __name__ == '__main__':
        main()

if __name__ == '__main__':
    unittest.main()