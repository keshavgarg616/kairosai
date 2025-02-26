from flask import Flask, render_template, request, redirect
from Event import Event

allEvents = []
app = Flask(__name__)

@app.route('/')
def home():
    global allEvents
    with open("Events.txt") as f:
        allEvents = eval(f.read())
    eventDays = [""] * 5
    days = ["mon", "tues", "wed", "thurs", "fri"]
    for i in range(len(allEvents)):
        event = allEvents[i]
        eventDays[days.index(event.day)] += f'''
                    <div class="event start-{event.startTime} end-{event.endTime} corp-fi" onclick="submit{event.name.replace(" ","")}Form()">
                        <form action="/event" id="{event.name}form" method="post">
                        <input type="hidden" id="event-name" name="event-name" value="{event.name}" />
                        <input type="hidden" id="comment" name="comment" value="" />
                        </form>
                        <p class="title">
                            {event.name}<br>
                            {event.startTime} {"AM" if event.startTime in ["9", "10", "11", "12"] else "PM"} - {event.endTime} {"AM" if event.endTime in ["9", "10", "11", "12"] else "PM"}
                        </p>
                    </div>
                    <script>
                    function submit{event.name.replace(" ","")}Form() {{
                        let form = document.getElementById("{event.name}form");
                        form.submit();
                    }}
                </script>
        '''
    return render_template('calender.html', monEvents = eventDays[0], tuesEvents = eventDays[1], wedEvents = eventDays[2], thursEvents = eventDays[3], friEvents = eventDays[4])

@app.route('/calenderTemp')
def calenderTemp():
    return render_template('calender.html')

@app.route('/event', methods=['GET', 'POST'])
def event():
    if request.method == 'POST':
        print("Post Request Received!!?!?!?")
        eventName = request.form['event-name']
        comment = request.form['comment']
        event = allEvents[0]
        for i in allEvents:
            if i.name == eventName:
                event = i
                break
        if comment != "":
            event.addComment(comment)
        comments = ""
        for i in event.forum:
            comments += f"<p class = 'posts'>{i}</p>"
        return render_template('event.html', eventName = eventName, comments = comments, AISummary = event.getSummary(), eventDetails = event.getDetails())
    else:
        return redirect("/")
    
@app.route('/addEvent', methods=['GET', 'POST'])
def addEvent():
    if request.method == 'GET':
        return render_template("add-event.html")
    else:
        name = request.form['event-name']
        tag = request.form['tag'].lower()
        day = request.form['day'].lower()
        day = {"monday":"mon", "tuesday":"tues", "wednesday":"wed", "thursday":"thurs", "friday":"fri", "mon":"mon", "tues":"tues", 
        "wed":"wed","thurs":"thurs","fri":"fri","thu":"thurs"}[day]
        startTime = request.form['start-timing']
        endTime = request.form['end-timing']
        allEvents.append(Event(name = name, tag = tag, day = day, startTime = startTime, endTime = endTime))
        with open("Events.txt", "w") as f:
            writeStr = "["
            for i in allEvents:
                writeStr += str(i) + ", "
            writeStr += "]"
            f.write(writeStr)
        return redirect("/")

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')

