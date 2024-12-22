# CLI Task Manager

## Описание

CLI Task Manager — это простое консольное приложение для управления задачами. Оно позволяет пользователям добавлять, обновлять, удалять и отслеживать статус задач. Это приложение разработано с использованием Python и SQLite для хранения данных.

## Функциональные возможности

- **Добавление задач**: Позволяет пользователю добавлять новую задачу с уникальным идентификатором.
- **Обновление задач**: Позволяет изменять название существующей задачи по её идентификатору.
- **Удаление задач**: Позволяет удалять задачу по её идентификатору.
- **Список задач**: Позволяет отображать все задачи с их текущим статусом.
- **Изменение статуса задач**: Позволяет пометить задачу как "в процессе" или "выполнена".

## Установка

1. Убедитесь, что у вас установлен Python (версия 3.6 и выше).
2. Склонируйте репозиторий:
```bash
   git clone https://github.com/kene33/cli-todo.git
   cd cli-todo
```
   

3. Установите необходимые зависимости (если есть):

   
```bash
   pip install -r requirements.txt
```

4. Запустите приложение из командной строки:
```bash
python cli_task.py <command> [options]
```

## Пример Использование
```bash
# Adding a new task
python main.py add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
python main.py update 1 "Buy groceries and cook dinner"
python main.py delete 1

# Marking a task as in progress or done
python main.py mark-in-progress 1
python main.py mark-done 1

# Listing all tasks
python main.py list

# Listing tasks by status
python main.py list done
python main.py list todo
python main.py list in-progress
```


## Идея взята с [roadmap.sh](https://roadmap.sh/projects/task-tracker). Более подробно можно узнать там. Приложение практически полностью идентично.


## Структура проекта

- cli_task.py: основной файл приложения.
- task_manager.py: содержит класс TaskManager, который управляет логикой задач.
- database.py: взаимодействует с базой данных SQLite для хранения и извлечения задач.

## Вклад

Если вы хотите внести свой вклад в проект, пожалуйста, создайте форк репозитория и отправьте пулл-запрос с вашими изменениями.

---

Это был оооочень оригинальный проект который еще никто не делал, честно.
   
