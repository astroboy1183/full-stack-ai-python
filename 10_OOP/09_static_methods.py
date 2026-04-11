class ChaiUtils:

    def clean_ingredients(self, text):
        return [item.strip() for item in text.split(",")]

raw = " water , milk,    ginger ,   cardamom"
obj = ChaiUtils()
print(obj.clean_ingredients(raw))

'''  Using static method below. '''
class ChaiUtils:

    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

raw = " water , milk,    ginger ,   cardamom"
obj1 = ChaiUtils()
print(obj1.clean_ingredients(raw))
print(ChaiUtils.clean_ingredients(raw))