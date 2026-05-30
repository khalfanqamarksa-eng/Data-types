def shut_down(shutdown):
    if shutdown == "yes":
        return "Shutting down"
    elif shutdown == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"
Answer = shut_down(str(input("Shut down computer? ")))
if Answer == "Shutting down":
    print(shut_down("yes"))
else:
    print(shut_down("no"))