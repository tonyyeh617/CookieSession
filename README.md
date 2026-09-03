# CookieSession Python ZIP distribution

CookieSession is a small Django project that demonstrates browser cookies and
server-side sessions. The ZIP download is a complete Django source tree: after
extracting it, install Django, run the migrations, and start the development
server.

## What's in the ZIP?

The archive contains the project package (`CookieSession`), the application
package (`CookieSessionApp`), HTML templates, the Django command-line entry
point, and the SQLite database used by the default settings. It is source
code, not a pre-built wheel or standalone executable. Python bytecode caches
(`__pycache__`) are generated locally and are not required for installation.

## File hierarchy

```text
CookieSession/
├── manage.py                    # Django administrative command-line entry point
├── db.sqlite3                   # SQLite database used by the default settings
├── CookieSession/
│   ├── __init__.py              # Marks the project package
│   ├── settings.py              # Installed apps, middleware, database, templates, and locale
│   ├── urls.py                  # URL routes for the admin site and demo views
│   └── wsgi.py                  # WSGI application for deployment
├── CookieSessionApp/
│   ├── __init__.py              # Marks the application package
│   ├── admin.py                 # Django admin registration module
│   ├── apps.py                  # Application configuration
│   ├── models.py                # Application data models (currently empty)
│   ├── tests.py                 # Django test module placeholder
│   ├── views.py                 # Cookie and session demonstration views
│   └── migrations/
│       └── __init__.py          # Migration package
├── templates/
│   ├── index.html               # Counter page rendered by the index view
│   ├── login.html               # Login/session demonstration page
│   └── testview.html            # Additional template available to the project
└── .vscode/
    └── launch.json              # Optional VS Code launch configuration
```

`__pycache__` directories and `.pyc` files may appear in a ZIP produced from a
working checkout. They are interpreter-generated caches and can safely be
deleted.

## Python package organization

`CookieSession` is the Django **project** package. It owns global settings,
URL routing, and the WSGI entry point. `CookieSessionApp` is the installed
Django **application** containing the example views. Templates live at the
top level because `settings.py` adds `templates/` to `TEMPLATES["DIRS"]`.

### Key modules

- `manage.py`: runs commands such as `migrate`, `runserver`, and `test`.
- `CookieSession/settings.py`: configures Django, SQLite, sessions, templates,
  Traditional Chinese locale (`zh-Hant`), and Taipei time zone.
- `CookieSession/urls.py`: maps HTTP paths to the functions in `views.py`.
- `CookieSession/wsgi.py`: exposes `application` for WSGI servers.
- `CookieSessionApp/views.py`: implements cookie operations, session
  operations, a daily visit counter, login/logout, voting, and small response
  examples.
- `db.sqlite3`: default local database. A new database can be created with
  `python manage.py migrate`.

## Requirements

- Python 3.6 or newer (the project uses f-strings and `pathlib`); use a
  Python version supported by the selected Django release.
- Django 2.2.x, matching the version family used to generate the project.
- A browser for trying the HTTP examples.

There is no `requirements.txt` in this distribution. Install Django into a
virtual environment rather than into the system interpreter:

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install "Django>=2.2,<3.0"
```

## Install and run from the ZIP

1. Extract the archive and change into the extracted directory (the directory
   containing `manage.py`).
2. Create and activate a virtual environment as shown above.
3. Install Django.
4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open <http://127.0.0.1:8000/index/> in a browser.

The included `db.sqlite3` is convenient for a demo. If it is absent or you
want a clean database, `migrate` creates the database configured in
`CookieSession/settings.py`.

## Quick start: try the endpoints

With the server running, these routes demonstrate the available behavior:

| URL | Purpose |
| --- | --- |
| `/index/` | Increment and display a daily `counter` cookie |
| `/set_cookie/<key>/<value>/` | Set a session cookie |
| `/set_cookie2/<key>/<value>/` | Set a cookie with a one-hour lifetime |
| `/get_cookie/<key>/` | Read one cookie |
| `/get_allcookies/` | List all request cookies |
| `/delete_cookie/<key>/` | Delete a cookie |
| `/set_session/<key>/<value>/` | Store a value in the Django session |
| `/set_session2/<key>/<value>/` | Store a value with a short expiry |
| `/get_session/<key>/` | Read one session value |
| `/get_allsessions/` | List session values |
| `/delete_session/<key>/` | Delete a session value |
| `/vote/` | Allow one vote per session |
| `/login/` | Display the demo login form |
| `/logout/` | Remove the demo login session value |
| `/admin/` | Django administration site |

For example, visit
`http://127.0.0.1:8000/set_cookie/favorite/chocolate/`, then
`http://127.0.0.1:8000/get_cookie/favorite/`. Values placed directly in a URL
should be URL-encoded when they contain spaces or reserved characters.

## Configuration and deployment notes

The defaults are intended for learning and local development. Before
deployment, change the generated `SECRET_KEY`, set `DEBUG = False`, restrict
`ALLOWED_HOSTS`, and configure a production database and static-file serving.
`wsgi.py` can be pointed at by a WSGI server after those settings are
reviewed. The example login credentials in `views.py` are demonstration data,
not an authentication system.
