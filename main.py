from datetime import datetime

def getNowString():
    return f"{datetime.now().date().year}.{datetime.now().date().month}.{datetime.now().date().day} {datetime.now().time().hour}:{datetime.now().time().minute}:{datetime.now().time().second}"

def printLog(text: str):
    print(getNowString(), "\033[32m" + "Log" + "\033[37m" + "     |" + "\033[90m", text, "\033[37m")

def printError(text: str):
    print(getNowString(), "\033[31m" + "Error" + "\033[37m" + "   |" + "\033[90m", text, "\033[37m")

def printWarning(text: str):
    print(getNowString(), "\033[33m" + "Warning" + "\033[37m" + " |" + "\033[90m", text, "\033[37m")

def printDebug(text: str):
    print(getNowString(), "\033[34m" + "Debug" + "\033[37m" + "   |" + "\033[90m", text, "\033[37m")
