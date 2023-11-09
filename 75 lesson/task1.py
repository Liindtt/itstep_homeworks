class EmailNotificationService:
    def send(self, message, receiver):
        print(f"Sending email: {message} to {receiver}")

class SmsNotificationService:
    def send(self, message, receiver):
        print(f"Sending SMS: {message} to {receiver}")

class NotificationService:
    def __init__(self, service):
        self.service = service

    def send_notification(self, message, receiver):
        self.service.send(message, receiver)


email_channel = EmailNotificationService()
sms_channel = SmsNotificationService()
notification_service = NotificationService(email_channel)
notification_service.send_notification("This is an email notification", "lindtt@google.com")
notification_service = NotificationService(sms_channel)
notification_service.send_notification("This is an SMS notification", "1234567890")
