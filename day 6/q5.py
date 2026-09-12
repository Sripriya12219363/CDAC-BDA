class Notifier:
    def __init__(self, sender_id, **kwargs):
        self.sender_id = sender_id
    def send(self, message):
        return [f"[Notifier {self.sender_id}] general broadcast: {message}"]
class EmailNotifier(Notifier):
    def __init__(self, email_server, **kwargs):
        self.email_server = email_server
        super().__init__(**kwargs)
    def send(self, message):
        logs = super().send(message)
        logs.insert(0, f"[Email via {self.email_server}] sending: {message}")
        return logs
class SMSNotifier(Notifier):
    def __init__(self, sms_gateway, **kwargs):
        self.sms_gateway = sms_gateway
        super().__init__(**kwargs)
    def send(self, message):
        logs = super().send(message)
        logs.insert(0, f"[SMS via {self.sms_gateway}] sending: {message}")
        return logs
class HybridAlertChannel(EmailNotifier, SMSNotifier):
    def __init__(self, sender_id, email_server, sms_gateway):
        super().__init__(
            email_server=email_server,
            sms_gateway=sms_gateway,
            sender_id=sender_id
        )
    def send(self, message):
        logs = super().send(message)
        logs.insert(0, "[HYBRID ALERT] Initiating dual channels...")
        return logs
def main():
    alert = HybridAlertChannel(
        sender_id="SYS-ADMIN",
        email_server="smtp.cdac.in",
        sms_gateway="gw.acts.com"
    )
    logs = alert.send("Disk space 95%")
    for log in logs:
        print(log)
    print(HybridAlertChannel.__mro__)
main()