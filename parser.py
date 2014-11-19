

def parse(strin):
    words = strin.split()
    state = 0 # 0 = getting verb, 1 = getting obj, 2 = getting iobj
    verb = ""
    obj = ""
    iobj = ""
    space = ""

    for word in words:
        if state == 0:
            verb = word
            state += 1
        elif state == 1:
            if word.lower() == "with":
                state += 1
                space = ""
                continue
            if word.lower() == "in":
                continue
            obj += space + word
            space = " "
        elif state == 2:
            iobj += space + word
            space = " "

    return (verb, obj, iobj)
