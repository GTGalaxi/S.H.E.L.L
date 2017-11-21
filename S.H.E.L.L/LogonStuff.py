import winsound, runpy, Mainframe, fileinput

def Fail():
    print("""
Incorrect username or password
Try again
""")
    winsound.PlaySound('SystemHand', winsound.SND_ALIAS)
    fileinput.close()
    runpy.run_path("Logon.py")
def Success(user):
    print("""
==============S.H.E.L.L==============

Welcome:
"""+user)
    winsound.PlaySound('SystemQuestion', winsound.SND_ALIAS)
    fileinput.close()
    Mainframe.Start()
def Admin():
    print("""
S.H.E.L.L Admin
Programs currently bugged or not functional:
* Remove user function - doesn't work, need to fix, if necessary remove user
  via user.txt.
* Shut down function - Doesn't work first time, if you wish to shutdown
  just do it twice. Same problem with force shutdown.
""")
    fileinput.close()
    Mainframe.Start()
