Calender Templates : https://freefrontend.co
*self.date = datem/css-calendars/

Event:
*self.name = name
*self.tag = tag
*self.date = date
*self.time = time
*self.forum = []
**getSummary()
**addComment()

ClubMeeting:
*self.name = meetingName
*self.tag = "meeting"
*self.date = "n/a"
*self.day = meetingDay
*self.time = meetingTime
*self.forum = []
**getSummary()
**addComment


Course:
*self.name = courseName
*self.tag = "course"
*self.date = "n/a"
*self.day = courseDay
*self.time = courseTime
*self.forum = []
*self.profs = []
**getSummary()
**addComment()
**setProfs()