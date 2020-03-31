gitrepo/
    azapp1/
        httpfunc1/-> (function runs at this context)
            core/p.py  (this is available?)
            main.py  ----> appends sys.path with configure_path and then calls its interface to config 
        httfunc2/
            main.py ----> appends sys.path with configure_path and then calls its interface to config
        cosmosfunc3/
            main.py ----> appends sys.path with configure_path and then calls its interface to config
        Dockerfile (at app level / not function level)
        corefn/
    azapp2/
        eventtrigger4/
            main.py ----> appends sys.path with configure_path and then calls its interface to config
    coreapp/
    configure_path.py ---> single point where sys.path gets appended with all the necessary app paths 