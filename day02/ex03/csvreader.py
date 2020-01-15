class CsvReader():
    def __enter__(self):
        try:
            self.fd = open(self.path, "r")
        except IOError:
            print("File not found")
            exit()
        return (self)

    def __exit__(self, type, value, traceback):
        self.fd.close()
   ########

    def __init__(self, path, sep=",", header=False, skip_Lop=0, skip_bottom=0):
        self.path = path
        self.__enter__()
        self.data = []
        self.head = header
        self.sep = sep
        self.nb_line = len(list(enumerate(self.fd)))
        self.skip_Lop = skip_Lop
        self.skip_bottom = skip_bottom
    
    def getdata(self):
        j = 0
        for count, el in enumerate(self.fd):
            if self.head == True and count == 0:
                self.header = el.split(self.sep)
                for i, elem in enumerate(self.header):
                    self.header[i] = self.header[i].strip().replace('"', '').replace('\n','')
            elif count >= self.skip_Lop + self.head and count < self.nb_line - self.skip_bottom:
                self.data.append(el.split(self.sep))
                j += 1
                for i, elem in enumerate(self.data[j - self.head]):
                    self.data[j - self.head][i] = self.data[j - self.head][i].strip().replace('"', '').replace('\n','')
        return(self.data)
    
    def getheader(self):
        return (self.header)

with CsvReader("good.csv",",", True,1,1) as file:
    data = file.getdata()
    header = file.getheader()

print(header)
print(data)
