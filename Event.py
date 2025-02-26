from ai_summary import getAISummary, getCourseDetails
from os import path

class Event:
    def __init__(self, name = "", tag = "", day = "mon", startTime = "", endTime = ""):
        self.name = name
        self.tag = tag
        self.day = day
        self.startTime = startTime
        self.endTime = endTime
        self.details = ""
        self.forumPath = "forums/" + name + ".txt"
        self.detailsPath = "details/" + name + ".txt"
        if path.exists(self.forumPath):
            with open(self.forumPath) as f:
                self.forum = eval(f.read())
        else:
            self.forum = []
            with open(self.forumPath, "w") as f:
                f.write("[]")

    def __str__(self):
        returnString = f'Event(name = "{self.name}", tag = "{self.tag}", day = "{self.day}", startTime = "{self.startTime}", endTime = "{self.endTime}")'
        return returnString
            
    def getSummary(self):
        return getAISummary(self.forum)

    def addComment(self, comment):
        self.forum.append(comment)
        with open(self.forumPath, "w") as f:
                f.write(str(self.forum))

    def getDetails(self):
        if path.exists(self.detailsPath):
            with open(self.detailsPath) as f:
                self.details = f.read()
        else:
            self.details = getCourseDetails(self.name)
            with open(self.detailsPath, "w") as f:
                f.write(self.details)
        return self.details