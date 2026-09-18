class ReportWriter:

    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "w", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

        print(f"Report saved successfully: {self.filename}")

        return False
    
