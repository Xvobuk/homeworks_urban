# Проверяем окейность сообщения
def okay(email):
    if "@" not in email:
        return False
    local_part, domain_part = email.split("@", 1)
    if "." not in domain_part:
        return False
    if not (domain_part.endswith(".com") or domain_part.endswith(".ru") or domain_part.endswith(".net")):
        return False
    return True

def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if not okay(sender) or not okay(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
