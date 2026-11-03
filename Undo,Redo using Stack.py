undo = []
redo = []

while True:
    print("1.Make Change 2.Undo 3.Redo 4.Display 5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        t = input("Enter text: ")
        undo.append(t)
        redo.clear()
    elif ch == 2:
        if undo:
            t = undo.pop()
            redo.append(t)
            print("Undone:", t)
        else:
            print("Nothing to undo")
    elif ch == 3:
        if redo:
            t = redo.pop()
            undo.append(t)
            print("Redone:", t)
        else:
            print("Nothing to redo")
    elif ch == 4:
        print("Document state:", " ".join(undo))
    elif ch == 5:
        break