from google import genai
from bs4 import BeautifulSoup
import requests

api_key = "YOUR API KEY HERE"
client = genai.Client(api_key = api_key)

def getAISummary(forum):
    request = "Summarize this in around 100 words about what happened during the week in this college course. This is a forum for the course."
    if len(forum) == 0:
        return "Not enough chat data to generate summary."
    for i in forum:
        request += f"\n{i}"
    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=request
    )
    return response.text

def getCourseDetails(courseID):
    r1 = requests.get('https://content.cs.umass.edu/content/spring-2025-course-descriptions')
    r2 = requests.get('https://content.cs.umass.edu/content/course-offering-plan')
    soup1 = BeautifulSoup(r1.content, 'html.parser')
    soup2 = BeautifulSoup(r2.content, 'html.parser')
    request = f"DO NOT USE any * characters. Give me a brief description listing prerequisites and course details for {courseID} from \n{soup1.prettify()}\n and \n{soup2.prettify()}\nas a bullet pointed list with <br> in place of \\n characters without any first person language."
    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=request
    )
    responseText = response.text
    responseText.replace('*', "")
    return responseText