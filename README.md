# google-cal-python

The end goal of the project is for our network monitoring solution to trigger a script when a device is restarted. Then trigger a second script after 10 minutes has passed. I referenced https://karenapp.io/articles/how-to-automate-google-calendar-with-python-using-the-calendar-api/ for the work.

The first script I uploaded (create_event_resource_craig.py) works as I'd hoped. It creates a Google calendar event, then overwrites the calendar event ID to the text file that I uploaded (created_event_id.txt).

The second script (delete_event_craig.py) is my problem. It will successfully delete the Google calendar event that the first script created. But I have to manually copy/paste the event ID from the "created_event_id.txt" into the proper location on line 12 of the script in order for it to work.

What I would love is to somehow allow "delete_event_craig.py" to import/reference/whatever-you-may-call-it the data string from the text file into the appropriate location of it's script. My apologies if this doesn't make sense, as I'm not a programmer....yet :) Thanks for any help you may offer!
