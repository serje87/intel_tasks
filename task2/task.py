"""Notes:
* One iteration of generator outputs N lines, where N is a given number of files
* TBD
"""
def open_files(file_list):
    opened_files = [open(file_) for file_ in file_list]
    while True:
        for f in opened_files:
            new_line = f.readline()
            if not new_line:
                f.seek(0)
                new_line = f.readline()
            print(new_line.rstrip("\n"))
        yield new_line
