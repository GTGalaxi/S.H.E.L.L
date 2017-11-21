import winsound, runpy, Mainframe

terminate = input("""
S.H.E.L.L program is currently running,
would you like to terminate it? (Y/N) """)
terminate = terminate.lower()

if terminate == str("n"):
    print("""Shutdown cancelled.
""")
    Mainframe.Start()
        
elif terminate == str("y"):
    print("""
S.H.E.L.L is shutting down.""")
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    runpy.run_path("ShutdownScreen.py")

else:
    Mainframe.Start()
    
    
