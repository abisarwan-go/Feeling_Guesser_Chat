
# Project Execution Instructions

To successfully run this project, please ensure that you have the following Python libraries installed:
- Daphne
- Channels

### Running the Servers

1. **Django Server:**
   ```bash
   python manage.py runserver
   ```

2. **WebSocket Server:**
   ```bash
   daphne -p 1999 chatDjango.asgi:application
   ```
