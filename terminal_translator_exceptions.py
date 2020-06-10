''' Кастомные исключения для программы '''

class LanguageDecectorError(BaseException): pass

class ArgumentError(BaseException): pass

class TextLengthError(BaseException): pass

class ConfigError(BaseException): pass

class TranslateError(BaseException): pass
