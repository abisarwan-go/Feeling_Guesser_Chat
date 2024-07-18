import subprocess
from django.core.management.commands.runserver import Command as RunServerCommand
from django.conf import settings
import socket

class Command(RunServerCommand):
    help = 'Starts the Django development server and Daphne.'

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            '--daphne-port', type=int, default=1030,
            help='Port to run Daphne on',
        )

    def handle(self, *args, **options):
        print("Custom runservers command is being executed")

        # Check if Daphne is already running on the port
        daphne_port = options['daphne_port']
        if not self.is_port_in_use(daphne_port):
            # Start the Daphne server in a separate process
            daphne_command = [
                'daphne', '-p', str(daphne_port), 'chatDjango.asgi:application'
            ]
            self.stdout.write(self.style.SUCCESS(f'Starting Daphne server on port {daphne_port}'))
            subprocess.Popen(daphne_command)
            print("Daphne process started")
        else:
            print(f"Port {daphne_port} is already in use. Skipping Daphne startup.")

        # Start the Django development server
        super().handle(*args, **options)
        print("Django development server started")

    def is_port_in_use(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0
