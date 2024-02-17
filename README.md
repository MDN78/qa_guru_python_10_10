## Jenkins + Selenoid

Ссылка на ресурс школы

[сайт jenkins](https://www.jenkins.io/)

[репозиторий jenkins](https://jenkins.autotests.cloud/)

[selenoid](https://selenoid.autotests.cloud/#/)

## Шаги
### Создаем задачу

Для создания новой задачи необходимо указать её название и выбрать параметр «Создать задачу со свободной конфигурацией». Нажимаем «OK».

Далее переходим во вкладку «Управление исходным кодом», выбираем «Git» и в поле вода вставляем ссылку на репозиторий. Нажимаем «Сохранить».

Так как на сервере могут работать несколько агентов под разные задачи, то во время настройки задачи необходимо указать актуального Jenkins-агента.
В нашем случае мы запускаем тесты на Python, поэтому переходим в настройки задачи, ставим галочку в поле «Ограничить лейблы сборщиков, которые могут исполнять данную задачу»
и в поле «Label Expression» вводим python. Нажимаем «Сохранить».

После этого необходимо добавить шаги сборки. Переходим во вкладку «Среда сборки». 
В выпадающем списке «Добавить шаг сборки» кликаем на «Добавить команду shell».

В появившемся поле вводим следующий скрипт:
```commandline
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```
Теперь добавим красивые Allure-отчёты. Для этого переходим во вкладку «Сборка», выбираем пункт «Добавить шаг после сборки» 
и в выпадающем списке кликаем на «Allure Report». </br> В поле «Path» проверяем, чтобы путь указывал на правильную директорию в проекте. 
Жмём «Сохранить»

Скорее всего Allure не будет показывать отчеты неавторизованным пользователям. 
Чтобы исправить, переходим в настройки, во вкладку «General» и выбираем пункт «Enable project-based security». 
В открывшемся меню проставляем галочку на пункте «Read» для анонимных пользователей. Жмем «Сохранить».

### Добавляем аттачменты

необходимо сперва добавить некоторые утилиты в код тестов. 
Для этого в директории `utils` в проекте создаем файл `attach.py` и пропишем в нём реализацию аттачментов:

```
import allure
from allure_commons.types import AttachmentType

# Скриншоты
def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

# логи
def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')

# html-код страницы
def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')

```

В коде тестов можно вызывать эти функции для добавления необходимых аттачей. К примеру:

```commandline
attach.add_html(browser)
attach.add_screenshot(browser)
attach.add_logs(browser)
```

## Selenoid

Для добавления Selenoid в проект переходим во вкладку «Capabilities», выбираем Python и копируем код с страницы

Далее код необходимо модернизировать:

```commandline
options = Options()
selenoid_capabilities = {
    "browserName": "chrome",
    "browserVersion": "100.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

options.capabilities,update(selenoid_capabilities)
driver = webdriver.Remote(
    command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
    options=options)

browser.config.driver = driver

```
После этого переходим в Jenkins и нажимаем «Собрать сейчас». Откроется подробный отчёт с аттачами.

### Добавляем видео

Для добавления видео заменим параметр enableVideo из кода выше на True:

```commandline
options = Options()
selenoid_capabilities = {
    "browserName": "chrome",
    "browserVersion": "100.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": True
    }
}

options.capabilities,update(selenoid_capabilities)
driver = webdriver.Remote(
    command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
    options=options)

browser.config.driver = driver
```

Далее в файле attach.py добавим соответствующую функцию:

```commandline
# скринкаст
def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')
```
Добавить видео в коде теста можно следующим образом:

```commandline
attach.add_video(browser)
```
