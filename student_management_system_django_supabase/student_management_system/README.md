# Student Management System — Django + Supabase

A colorful, responsive student CRUD dashboard built with Django, HTML/CSS, and Supabase PostgreSQL.

## Features
- Public landing page and separate login/logout flow
- Django admin panel at `/admin/`
- Staff-only dashboard and student CRUD (Create, Read, Update, Delete)
- Standard user dashboard showing students they added
- Search students by name, email, course, or student ID
- Responsive neon-gradient UI
- Django authentication, password hashing, CSRF protection, and server-side permissions
- Supabase PostgreSQL database connection through `DATABASE_URL`

## Important architecture note
This starter uses **Django authentication** for login/logout/admin and **Supabase PostgreSQL** as the database. It does not use Supabase Auth. This keeps the two role types straightforward for a Django learning project. The database password must remain server-side in `.env`; never put it in HTML or JavaScript.

## 1. Requirements
- Python 3.10+
- A Supabase project (or use SQLite locally if you leave `DATABASE_URL` empty)
- Windows PowerShell / Command Prompt

## 2. Extract and open the project
Extract the ZIP, then open a terminal in the `student_management_system` folder.

### Windows PowerShell
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

If PowerShell blocks activation, use Command Prompt:
```bat
py -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
```

## 3. Connect Supabase (optional but recommended)
1. Open your Supabase dashboard and create/open your project.
2. Click **Connect** and copy the **Session pooler** PostgreSQL connection string (port `5432`), or use the direct connection if your network supports it.
3. Open `.env` and set `DATABASE_URL` to that connection string. Ensure it includes `?sslmode=require`.
4. Keep the password private. Do not share `.env` or commit it to Git.
5. If you leave `DATABASE_URL` blank, the project uses local SQLite for practice.

Example format only — replace every placeholder:
```text
DATABASE_URL=postgresql://postgres.PROJECT_REF:YOUR_PASSWORD@aws-0-region.pooler.supabase.com:5432/postgres?sslmode=require
```

## 4. Create database tables and admin
```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
Enter your own username, email, and password when prompted.

## 5. Run the project
```powershell
python manage.py runserver
```

Open:
- Landing page: http://127.0.0.1:8000/
- Login: http://127.0.0.1:8000/accounts/login/
- User dashboard: http://127.0.0.1:8000/dashboard/
- Django admin: http://127.0.0.1:8000/admin/

## 6. Roles
- **Admin/staff:** Create a superuser using `createsuperuser`; can access Django admin and manage all students.
- **Normal user:** Register at `/accounts/register/`; can see students they created and add new students. Only staff can edit/delete any student from the management interface.
- **Staff dashboard:** Staff can view all students and create, update, and delete student records.

## 7. Demo workflow
1. Create a superuser.
2. Sign in at `/accounts/login/`.
3. Use the dashboard to add students.
4. Search and test edit/delete (staff only).
5. Open `/admin/` to see Django's admin panel.

## Troubleshooting
- `psycopg` connection errors: check `DATABASE_URL`, password encoding, Supabase project status, and that `sslmode=require` is present.
- Supabase host/network errors: use the Session pooler connection string shown in your dashboard.
- `DisallowedHost`: add your host to `ALLOWED_HOSTS` in `.env`.
- PowerShell activation issue: use Command Prompt commands shown above.
- To reset local practice data, stop the server and delete `db.sqlite3`, then run migrations again. Do not delete your Supabase database to reset a demo.
