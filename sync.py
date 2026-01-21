import os
import requests
import datetime
from icalendar import Calendar
from dotenv import load_dotenv

load_dotenv()
CANVAS_ICAL_URL = os.environ["CANVAS_ICAL_URL"]
NTFY_TOPIC = os.environ["NTFY_TOPIC"]

now = datetime.datetime.now(datetime.timezone.utc)
classes = ["CIS4930", "CIS4250", "COP4710"]


def sync():
    res = requests.get(CANVAS_ICAL_URL)
    res.raise_for_status()

    cal = Calendar.from_ical(res.content)

    assignments = []

    for component in cal.walk():
        if component.name == "VEVENT":
            summary = component.get("summary", "")
            if any(word in summary for word in classes):
                due_date = component.get("dtstart").dt

                if isinstance(due_date, datetime.date) and not isinstance(
                    due_date, datetime.datetime
                ):
                    due_date = datetime.datetime.combine(
                        due_date, datetime.time.min
                    ).replace(tzinfo=datetime.timezone.utc)

                if now.date() == due_date.date():
                    assignments.append(summary)

    if len(assignments):
        requests.post(
            "https://ntfy.sh/" + NTFY_TOPIC,
            data="\n\n".join(assignments),
            headers={
                "Title": f"{len(assignments)} assignments are due today!",
                "Priority": "urgent",
                "Tags": "warning, rotating_light",
                "Click": "canvas-student://usflearn.instructure.com/"
            },
        )


if __name__ == "__main__":
    sync()