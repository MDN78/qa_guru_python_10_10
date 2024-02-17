## Задание 10 и Задание 12 - Jenkins

Провести рефакторинг своего теста на регистрацию студента по форме `https://demoqa.com/automation-practice-form` 

Используя инструменты объектно-ориентированной парадигмы для инкапсуляции деталей реализации бизнес-шагов пользователя, таким образом реализовав идеи шаблона PageObject.

### Часть 1 branch mid-level-step-objects

[mid-level-step-objects](https://github.com/MDN78/qa_guru_python_10_10/tree/mid-level-step-objects)

В этой части мы рассматриваем как ценный c точки зрения бизнеса шаг пользователя – «заполнение отдельных данных о пользователе» или «подтверждение результата проделанной работы» (как например, подтверждение что регистрация прошла успешно).


### Часть 2 branch high-level-step-objects

[high-level-step-objects](https://github.com/MDN78/qa_guru_python_10_10/tree/high-level-step-objects)

В этой части мы рассматриваем как ценный c точки зрения бизнеса шаг пользователя – «отправить форму с данными» или другими словами «провести регистрацию через форму». Также шагом считаем подтверждение результата проделанной работы (как например, подтверждение, что регистрация прошла успешно).

Также в этой части следует провести рефакторинг работы с данными пользователя, представив их в виде объекта датакласса

### Часть 3 branch application-manager

[branch application-manager](https://github.com/MDN78/qa_guru_python_10_10/tree/application-manager)

* добавить в проект тест на упрощенную регистрацию через форму https://demoqa.com/text-box  и соответствующий PageObject. 

* Реализовать шаблон ApplicationManager для предсоздания всех объектов для пейдж-обджектов.

* в тесте загрузить форму не через simple_registration_form.open(), а через app.left_panel.open_simple_registration_form(), который должен быть шорткатом (методом, вызывающим под капотом другой метод этого же объекта) на app.left_panel.open('Elements', 'Text Box')

* cоответственно добавить пейджобджект для LeftPanel и создать его объект в виде поля обьекта апликейшен-менеджера

### Часть 4 Jenkins + Selenoid

[jenkins-high-level-step-objects](https://github.com/MDN78/qa_guru_python_10_10/tree/jenkins-high-level-step-objects)