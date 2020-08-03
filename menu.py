import os


class Menu:
    __currentDirs = {}
    __location = []

    def __init__(self, path):
        assert isinstance(path, str)
        self.__location = list(map(str, path.split('/')))

    def starter(self):
        self.__printDirsAndFiles(self.__getPath())
        self.__waiter()

    def searcher(self, file_name):
        print(self.__getPath())
        for root, dirs, files in os.walk(self.__getPath()):
            print(root)
            for file in files:
                print(file)
                if file == file_name:
                    self.__printFileContent(os.path.join(root, file))
                    return
        print("nothing found! check input " + file_name)

    def __printDirsAndFiles(self, path):
        lst = os.listdir(path)
        if len(lst) == 0:
            self.__location.pop()
            print("no content in directory enter something else")

        else:
            for key in range(len(lst)):
                self.__currentDirs[key] = lst[key]
                print("{0}. {1}".format(key, lst[key]))
        self.__waiter()

    def __printFileContent(self, path):
        file = open(os.path.abspath(path), "r")
        for line in file.readlines():
            print(line)

    def __getPath(self):
        path = "/"
        path = path.join(self.__location)
        return path

    def __waiter(self):
        user_input = input()

        if user_input == "..":
            self.__location.pop()
            self.__printDirsAndFiles(self.__getPath())
            return

        try:
            user_input = int(user_input)
        except TypeError:
            print("please enter valid")
            self.__printDirsAndFiles(self.__getPath())
            return

        for key, value in self.__currentDirs.items():
            if key == user_input:
                if os.path.isdir(os.path.join(self.__getPath(), value)):
                    self.__location.append(value)
                    self.__printDirsAndFiles(os.path.join(self.__getPath()))
                else:
                    self.__printFileContent(os.path.join(self.__getPath(), value))
                    self.__printDirsAndFiles(os.path.join(self.__getPath()))
                break
        return
