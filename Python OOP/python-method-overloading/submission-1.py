class TextProcessor:
    # def format_text(self, a):
    #     return a.upper()

    def format_text(self, a, b=None):
        if b is None:
            return a.upper()
        c = a+b
        return c
    



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
