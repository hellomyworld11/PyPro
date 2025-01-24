
import ui
import models


def main():
    print("入口")
    dic = models.create_dictionnary()
    print(dic)
    keylist = list(dic.keys())
    mainframe = ui.MainWindow(keylist, dic)
    mainframe.create()
    mainframe.mainloop()


if __name__ == "__main__":
    main()