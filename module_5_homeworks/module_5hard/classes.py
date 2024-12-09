import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    @staticmethod
    def hash_password(password):
        return int(hashlib.md5(password.encode()).hexdigest(), 16)

    def __repr__(self):
        return self.nickname # Вот здесь всё-таки надо поменять было на никнейм, фух, конец


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})"


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = User.hash_password(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Добро пожаловать, {nickname}!")
                return
        print("Неверный логин или пароль.")

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):
        if self.current_user:
            print(f"До свидания, {self.current_user.nickname}!")
            self.current_user = None
        else:
            print("Вы не вошли в аккаунт.")

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_term):
        search_term = search_term.lower()
        return [video.title for video in self.videos if search_term in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    # А мы точно Ютюб создаём, а не Порнхаб?
                    return

                print(f"Воспроизведение видео: {title}")
                for second in range(video.time_now + 1, video.duration + 1):
                    print(second, end=" ", flush=True)
                    time.sleep(0.5)
                print("Конец видео", end="\n")
                video.time_now = 0
                return

        # print("Видео не найдено.")
        # На всякий случай оставлю тут закомментированным, потом уберу