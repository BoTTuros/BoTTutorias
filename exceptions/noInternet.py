class NoIssueException(exception):
    def __init__(self,*args,**kwargs):
        exception.__init__(self,"Internet connection error")
