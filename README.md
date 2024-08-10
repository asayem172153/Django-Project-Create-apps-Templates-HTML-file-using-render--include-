# Django Project Overview

This Django project demonstrates the basics of setting up a web application with multiple apps, configuring templates, and rendering HTML files. Below is a quick summary of the features implemented:

- **Create Apps**
- **Configure Template Folder**
- **Create HTML Files for All Apps**
- **Use `render()` Function**
- **Use `include()` Function**

---

## 🚀 Quick Start

To get started with this project:
---

## 📂 Project Structure

- **Project Initialization:**
  - This project was created using `django-admin startproject`, setting up the base project structure.
  
- **App Creation:**
  - Created multiple Django apps using `python manage.py startapp app_name`. Each app is designed to handle specific functionalities of the project.

- **Template Configuration:**
  - Configured the global template directory in `settings.py`:
    ```python
    
    TEMPLATE_DIR = BASE_DIR/'templates'
    
    TEMPLATES = [
        {
            ...
            'DIRS': [TEMPLATE_DIR],
            ...
        },
    ]
    ```

- **HTML Files for All Apps:**
  - For each app, HTML files were organized in a `templates` directory with the structure:
    ```
    /app_name/templates/app_name/template_name.html
    ```
  
- **Rendering Views with `render()` Function:**
  - Used the `render()` function in `views.py` to load and display HTML templates:
    ```python
    def home(request):
        return render(request, 'app_name/home.html')
    ```

- **Reusing Templates with `include()` Function:**
  - Included reusable components like navigation bars across multiple pages using `{% include %}` in templates:
    ```html
    {% include 'app_name/navbar.html' %}
    ```

---

## 🛠️ Technologies Used

- **Django**: High-level Python web framework
- **Python**: Programming language
- **HTML**: Markup language for creating web pages

---


## 📞 Contact

For any inquiries, feel free to reach out:

- **Email**: abusayem379@gmail.com
- **LinkedIn**: https://www.linkedin.com/in/abusayem172153/

---

*This project showcases foundational Django skills, perfect for those getting started with web development!*

