import runpy, enchant, Mainframe

def Search(program, caller):
    
    search = input("""
>>> """)
    search = search.lower()
    search = search.replace(" ","")

    ProgList = enchant.request_pwl_dict(program+".txt")

    CheckProg = ProgList.check(search)

    suggested = str(ProgList.suggest(search))
    suggested = suggested.strip("[")
    suggested = suggested.strip("]")
    suggested = suggested.strip("'")

    if CheckProg == False:
        print("""
That is an unrecognised function,""")
        print("""Did you mean:
""" + suggested + "?")
        Search(program, caller)
    else:
        if search == ("exit"):
            Mainframe.Start()
        else:
            search = search+".py"
            runpy.run_path(search)
