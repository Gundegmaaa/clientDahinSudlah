from django.shortcuts import render

BLOGS = [
    {
        "id": 1,
        "title": "Django Template яагаад чухал вэ?",
        "content": "Template ашигласнаар бизнес логик болон харагдац салж, код илүү цэгцтэй, засварлахад хялбар болдог.",
        "author": "Бат",
    },
    {
        "id": 2,
        "title": "Django дээр URL routing-ийн үндэс",
        "content": "urls.py файл нь орж ирсэн замуудыг view функцтэй холбож, хэрэглэгчид зөв хариу буцаадаг.",
        "author": "Сараа",
    },
    {
        "id": 3,
        "title": "Bootstrap ашиглаад UI хурдан хийх нь",
        "content": "Bootstrap-ийн бэлэн компонентуудыг ашигласнаар лабораторийн ажлын front-end-ийг хурдан бүтээх боломжтой.",
        "author": "Тэмүүлэн",
    },
    {
        "id": 4,
        "title": "Монгол хэлтэй контент бэлтгэх зөвлөмж",
        "content": "Вэб дээр монгол хэлний контент оруулахдаа утга ойлгомжтой гарчиг, товч дэд тайлбар, уншихад хялбар бүтэц ашиглах хэрэгтэй.",
        "author": "Оюунаа",
    },
    {
        "id": 5,
        "title": "Django view-ээс template рүү өгөгдөл дамжуулах",
        "content": "View дотор dictionary эсвэл list бэлдээд render функцээр template рүү context хэлбэрээр дамжуулснаар динамик хуудас үүсгэнэ.",
        "author": "Мөнх-Эрдэнэ",
    },
]


def blog_list(request):
    return render(request, "blog/blog_list.html", {"blogs": BLOGS})


def blog_detail(request, blog_id):
    blog = next((item for item in BLOGS if item["id"] == blog_id), None)
    return render(request, "blog/blog_detail.html", {"blog": blog})
