class Evaluator:
    """My evaluator"""
    @staticmethod
    def zip_evaluate(coefs, words):
        if isinstance(coefs, list) == 0 or isinstance(words, list) == 0:
            print("Both params should be lists")
        elif len(coefs) != len(words):
            print("Error, lists are not the same size")
        else:
            for coef in coefs:
                if isinstance(coef, float) == 0:
                    print("Coefs should only be float")
                    return
            for word in words:
                if isinstance(word, str) == 0:
                    print("Words should only be string")
                    return
            couple = zip(coefs, words)
            res = 0
            i = 0
            for word in words:
                res += couple[i][0] * len(couple[i][1])
                i += 1
            print(res)

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if isinstance(coefs, list) == 0 or isinstance(words, list) == 0:
            print("Both params should be lists")
        elif len(coefs) != len(words):
            print("Error, lists are not the same size")
        else:
            for coef in coefs:
                if isinstance(coef, float) == 0:
                    print("Coefs should only be float")
                    return
            for word in words:
                if isinstance(word, str) == 0:
                    print("Words should only be string")
                    return
            coef = enumerate(coefs)
            word = enumerate(words)
            res = 0
            for count, ele in enumerate(coefs):
                res += ele * len(list(enumerate(words))[count][1])
            print(res)

coef = [1.0,2.0,3.0,0.0,10.0]
word = ["je","o","al","coucou","ma"]
print("By zip:")
Evaluator.zip_evaluate(coef, word)
print("By enumerate:")
Evaluator.enumerate_evaluate(coef, word)
