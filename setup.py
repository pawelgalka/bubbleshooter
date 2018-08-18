import cx_Freeze  #for now, do the wildcard import, though the bigger the script gets, I would recommend an as ... structure

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Bubble shooter",
    author = "Pawel Galka",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["arrow.png"]}},
    executables = executables,
    version = "1.0.0"
    )