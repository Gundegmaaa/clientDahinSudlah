## Lab 10 (Django ModelForm CRUD)

### Ажиллуулах

```bash
cd lab10
source .venv/bin/activate
cd news_site
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### URL-ууд

- `http://127.0.0.1:8000/` — мэдээ жагсаалт
- `http://127.0.0.1:8000/news/add/` — мэдээ нэмэх
- `http://127.0.0.1:8000/admin/` — admin (Category, News)

### Тайлбар

- **Models**: `Category(name)`, `News(title, content, created_at readonly, category)`
- **Form**: `NewsForm` (ModelForm)
- **CRUD**: нэмэх/засах/устгах + жагсаалт
