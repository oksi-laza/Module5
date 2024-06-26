from time import sleep    # для паузы между выводами секунд воспроизведения


class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль, возраст
    """
    def __init__(self, nickname, hash_password, age):   # hash_password - пароль в хэшированном виде
        self.nickname = nickname
        self.password = hash_password
        self.age = age

    def __str__(self):        # при выводе на экран объекта этого класса, будет возвращаться nickname(логин)
        return self.nickname


class Video:
    """
    Класс, содержащий название видео, его продолжительность (в сек.), ограничение по возрасту и секунду остановки.
    title - заголовок
    duration - продолжительность, секунды
    time_now - секунда остановки (изначально 0)
    adult_mode - ограничение по возрасту (изначально False)
    """
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    """
    Класс для регистрации и авторизации пользователей/сброса пользователя.
    Для поиска и добавления видео. Для воспроизведения времени просмотра найденного видео.
    """
    def __init__(self):
        self.users = []     # создали пустой список пользователей,будет пополняться зарегистрированными пользователями
        self.videos = []    # создали пустой список объектов Video, который будет пополняться новыми видео
        self.current_user = None    # текущий пользователь User изменится на найденного - авторизовавшегося пользователя

    def log_in(self, login, password):    # Вход в аккаунт. Находит пользователя в users с такими же логином и паролем
        hash_password = hash(password)
        check_log_in = False
        for user in self.users:
            if user.nickname == login and user.password == hash_password:
                check_log_in = True
                break       # после того, как нашлось совпадение по логину и соответствующему паролю, останавливает цикл
            else:
                check_log_in = False
        if check_log_in == True:
            self.current_user = user
            print(f'{self.current_user}, добро пожаловать!')
        else:
            print('Логин или пароль не найдены')

    def register(self, nickname, password, age):    # Регистрация аккаунта и автоматический вход.
        self.age = age
        hash_password = hash(password)
        new_user = User(nickname, hash_password, self.age)
        check_new_user = False
        if self.users == []:
            self.users.append(new_user)
            self.current_user = nickname
        else:
            for user in self.users:
                if user.nickname != nickname:
                    check_new_user = True
                else:
                    check_new_user = False
                    break
            if check_new_user == True:
                self.users.append(new_user)
                self.current_user = nickname
            else:
                print(f'Пользователь {nickname} уже существует')

    def log_out(self):    # для сброса текущего пользователя
        self.current_user = None

    def add(self, *videos):
        """
        :param videos: принимает любое кол-во объектов класса Video
        и добавляет их в self.videos, если с таким же названием видео ещё не было в списке
        :return: self.videos
        """
        check_video = False
        for video in videos:
            name_video = video.title.lower()   # сохранили в переменной название видео из объекта для сравнения в списке
            # print(video)              # вывод на экран объектов
            # print(name_video)         # вывод на экран название видео в нижнем регистре
            if self.videos == []:
                self.videos.append(video)
                # print(self.videos)      # проверила, что объект добавился
            else:
                for video_in_list in self.videos:
                    if video_in_list.title.lower() != name_video:    # сравнение названия видео из списка с добавляемым
                        check_video = True
                    else:
                        # print(video_in_list.title.lower(), name_video)   # проверка какие видео одинаковые по названию
                        check_video = False
                        break
                if check_video == True:
                    self.videos.append(video)
        # return print(self.videos)    # когда хочу проверить, сколько объектов в списке
        return self.videos


    def get_videos(self, word):
        """
        :param word: принимает поисковое слово
        Поиск ведётся без учета регистра.
        :return: возвращает список названий всех видео, содержащих поисковое слово
        """
        self.word = word.lower()
        video_titles = []
        for video in self.videos:
            name_video = video.title.lower()
            if self.word in name_video:
                video_titles.append(video.title)
        return video_titles

    def watch_video(self, title_video):
        """
        :param title_video: название фильма
        Если находит название видео, ведётся отсчёт времени в консоль на какой секунде ведётся просмотр.
        После текущее время просмотра данного видео сбрасывается.
        """
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for video in self.videos:
                if video.title == title_video:
                    if self.age < 18 and video.adult_mode == True:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        # ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
                        for time_position in range(video.duration):
                            sleep(1)
                            video.time_now += 1
                            print(video.time_now, end=' ')
                        print('Конец видео')
                        video.time_now = 0



# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Для чего девушкам парень программист?', 20, adult_mode=True)

# Добавление видео
ur.add(v1, v2, v3)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')



# # Дополнительный код для проверки (для себя)
# # Проверка входа по логину и паролю
# ur.log_out()
# print('1 выход - пользователь:', ur.current_user)
# ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
# print('1 вход по логину и паролю - пользователь:', ur.current_user)
#
# ur.log_out()
# print('2 выход - пользователь:', ur.current_user)
# ur.log_in('vasya_pupkin', 'lolkekcheburek',)
# print('2 вход по логину и паролю - пользователь:', ur.current_user)
#
# ur.log_out()
# print('3 выход - пользователь:', ur.current_user)
# ur.register('Oksana', 'iSjdfkfhkdhg', 36)
# print('3 вход по логину и паролю - пользователь:: ', ur.current_user)
#
# ur.log_out()
# print('4 выход - пользователь:', ur.current_user)
# ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
# print('4 вход по логину и паролю - пользователь:', ur.current_user)