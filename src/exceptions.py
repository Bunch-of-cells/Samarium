def handle_exception(exception: Exception):
    name = exception.__class__.__name__
    if name != "NotDefinedError":
        if not name.startswith("Samarium"):
            name = "External" + name
        else:
            name = name.removeprefix("Samarium")
    color = f"\033[{4 - (name == 'Error')}1m"
    print(f"{color}[{name}] {exception}\033[0m")
    exit(1)


class NotDefinedError(Exception):
    def __init__(self, class_, message: str):
        self.class_ = class_.__class__.__name__
        super().__init__(f"{self.class_}.{message}")


class SamariumError(Exception):
    blank = ""
    prefix = ""

    def __init__(self, message: str = ""):
        super().__init__(f"{self.prefix}{message}" or self.blank)


class SamariumImportError(SamariumError):
    blank = "Import error"
    prefix = "Invalid module: "


class SamariumSyntaxError(SamariumError):
    blank = "Invalid syntax"
    prefix = "Unsupported character: "


class SamariumTypeError(SamariumError):
    blank = "Invalid type"
    prefix = "Unsupported type: "