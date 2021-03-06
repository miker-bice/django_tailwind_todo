
# Django - Tailwind Todo App

A complete todo app with user authentication and
registrartion built with Django and Tailwind




## Features

- Light/dark mode styling
- Mobile Responsive
- User Registration & Authentication
- Custom user Todo lists


## Tech Stack

**Front-end:** HTML, CSS, TailwindCSS

**Back-end:** Python & Django


## Documentation

**Database Structure**

![database-structure](https://github.com/miker-bice/django_tailwind_todo/blob/main/readMe/database-structure.jpg)

This is the database structure of the App. It consists of two database models, the <strong>User Model</strong>
and the <strong>Todo List Model</strong>. The Todo list contains different fields one of them is the target_id
field which has a <strong>One-to-Many relationship</strong> with the ID field in the <strong>User Model</strong>

This database structure allows saving of todo tasks that are specific to the user who created the task

**Sitemap**

![sitemap](https://github.com/miker-bice/django_tailwind_todo/blob/main/readMe/django_tailwind_todo_sitemap.jpg)

This is the sitemap of the web app. The whole projects contains two seperate apps, the <strong>Authentication App</strong>
used for <em>user authentication & registration</em> and the <strong>Todo App</strong> which display the user's todo list
and has the capability to add, edit and delete tasks.

## Authors

- [@miker-bice](https://www.github.com/miker-bice)


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

