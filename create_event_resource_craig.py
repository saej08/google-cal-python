from datetime import datetime, timedelta
from cal_setup import get_calendar_service


def main():
   # creates one hour event tomorrow 10 AM EST
   service = get_calendar_service()

   d = datetime.now().date()
   tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=1)).isoformat()

   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": 'Automating calendar',
           "description": 'This is a tutorial example of automating google calendar with python',
           "start": {"dateTime": start, "timeZone": 'US/Eastern'},
           "end": {"dateTime": end, "timeZone": 'US/Eastern'},
           "attendees": [
              {
      "email": "example@cru.org",
      "displayName": 'example-room',
       }
    ]
   }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   with open('created_event_id.txt', 'w') as f:
      print(event_result['id'], file=f)
   print(event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

if __name__ == '__main__':
   main()
