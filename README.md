### 📌 **Maha Real Estate - Real Estate enrollment System**  
_A Django-based web application with MySQL backend, user authentication, and role-based access control._

---

## 🚀 **Project Overview**  
Maha Real Estate is a web-based platform designed to simplify real estate management by providing a seamless interface for property buying, user registration, and application tracking. The system includes user authentication (login/logout), authorized user registration, and a secure MySQL database.

---

## 📋 **Features**  
✅ **User Authentication**: Login, logout, and secure password management  
✅ **Authorized Registration**: Admin approval for new user registrations  
✅ **Application Tracking**: Track submission, verification, and acceptance status  
✅ **Admin Dashboard**: Manage users, properties, and applications  
✅ **Responsive UI**: Mobile-friendly design  

---

## ⚙ **Tech Stack**  

| Technology  | Description  |
|-------------|--------------|
| **Django** | Backend framework (Python) |
| **MySQL** | Relational database management system |
| **HTML/CSS/Bootstrap** | Frontend styling |
| **JavaScript (Optional)** | Enhancements for interactivity |
| **Postman** | API testing |
| **Git & GitLab/GitHub** | Version control |

---

## 🛠 **Installation & Setup**  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/yourusername/real-estate-django.git
cd real-estate-django
```

### 2️⃣ Set Up a Virtual Environment  
```sh
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3️⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```

### 4️⃣ Configure the Database  
- Update `settings.py` with your MySQL credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'real_estate_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
- Run migrations:  
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a Superuser  
```sh
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

### 6️⃣ Run the Development Server  
```sh
python manage.py runserver
```
Access the application at **`http://127.0.0.1:8000/`**.

---

## 🔑 **Usage Guide**  
### 🔹 **User Roles**  
- **Admin**: Can manage users, approve registrations, and oversee property documentries  
- **Registered Users**: Can buy properties, track applications, and view status updates    

---

## 🤝 **Contributing**  
1. Fork the repository  
2. Create a new branch (`feature-branch`)  
3. Commit changes and push to your fork  
4. Submit a Pull Request  

