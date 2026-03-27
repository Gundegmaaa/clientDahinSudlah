from django.shortcuts import render

ZODIACS = [
    {"id": 1, "name": "Хулгана", "description": "Сэргэлэн, шаламгай, арга ухаантай.", "element": "Ус"},
    {"id": 2, "name": "Үхэр", "description": "Тэвчээртэй, найдвартай, хөдөлмөрч.", "element": "Шороо"},
    {"id": 3, "name": "Бар", "description": "Зоригтой, эрч хүчтэй, өрсөлдөх дуртай.", "element": "Мод"},
    {"id": 4, "name": "Туулай", "description": "Зөөлөн, эелдэг, ухаалаг.", "element": "Мод"},
    {"id": 5, "name": "Луу", "description": "Өөртөө итгэлтэй, нэр төртэй, манлайлагч.", "element": "Шороо"},
    {"id": 6, "name": "Могой", "description": "Зөн совин сайтай, тайван, бодлоготой.", "element": "Гал"},
    {"id": 7, "name": "Морь", "description": "Эрч хүчтэй, эрх чөлөөт, өөдрөг.", "element": "Гал"},
    {"id": 8, "name": "Хонь", "description": "Бүтээлч, энэрэнгүй, дөлгөөн.", "element": "Шороо"},
    {"id": 9, "name": "Бич", "description": "Сониуч, авхаалжтай, сэргэлэн.", "element": "Төмөр"},
    {"id": 10, "name": "Тахиа", "description": "Шударга, нямбай, ажилсаг.", "element": "Төмөр"},
    {"id": 11, "name": "Нохой", "description": "Үнэнч, хамгаалагч, шулуун шударга.", "element": "Шороо"},
    {"id": 12, "name": "Гахай", "description": "Өгөөмөр, дулаахан сэтгэлтэй, чармайлттай.", "element": "Ус"},
]


def zodiac_list(request):
    return render(request, "zodiac/zodiac_list.html", {"zodiacs": ZODIACS})


def zodiac_detail(request, zodiac_id):
    zodiac = next((item for item in ZODIACS if item["id"] == zodiac_id), None)
    return render(request, "zodiac/zodiac_detail.html", {"zodiac": zodiac})
