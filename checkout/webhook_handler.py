from django.http import HttpResponse


class StripeWH_handler:

    def __init(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'webhook recieved: {event["type"]}',
            status=200
        )
