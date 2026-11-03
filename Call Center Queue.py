calls = []

def addCall(cid, t):
    calls.append((cid, t))
    print("Call added: Customer", cid, "-", t, "min")

def answerCall():
    if calls:
        cid, t = calls.pop(0)
        print("Answered call of Customer", cid, "-", t, "min")
    else:
        print("No calls to answer")

def viewQueue():
    print("Calls in queue:", calls)

def isQueueEmpty():
    return len(calls) == 0

addCall(101, 5)
addCall(102, 3)
addCall(103, 8)
viewQueue()
answerCall()
print("Is queue empty?", isQueueEmpty())
answerCall()
answerCall()
print("Is queue empty?", isQueueEmpty())
answerCall()