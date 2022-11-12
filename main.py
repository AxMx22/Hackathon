
def file_import(name):
    try:
        file = open (name, "r")
    except:
        print("Invalid File Format")
        return None

    return file

