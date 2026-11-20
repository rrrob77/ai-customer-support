def email(sender: str, subject: str, body: str) -> str:
    #Format a test email the same way format_thread formats a Gmail thread
    return f"Subject: {subject}\n\nCustomer ({sender}):\n{body}"


GOLDEN_EMAILS = [
    {
        "name": "board-size-90kg",
        "email": email("Tom Becker <tom@example.com>", "Which board?",
                       "Hi, I weigh about 90 kg. Which of your paddle boards should I buy?"),
        "section": "paddle-boards", "action": "reply"
    },
    {
        "name": "board-size-german",
        "email": email("Lena Vogel <lena@example.com>", "Welche Größe?",
                       "Hallo, ich wiege 70 kg und bin Anfängerin. Welches Board passt zu mir?"),
        "section": "paddle-boards", "action": "reply"
    },
    {
        "name": "pump-missing-with-order",
        "email": email("Sam Lee <sam@example.com>", "No pump in the box",
                       "My 11' board arrived without the pump. Order 112-4839201-5528341."),
        "section": "paddle-boards", "action": "escalate"
    },
    {
        "name": "pump-missing-no-order",
        "email": email("Sam Lee <sam@example.com>", "Pump missing",
                         "Hi, the pump was not in the box. What now?"),
        "section": "paddle-boards", "action": "reply"
    }
]
