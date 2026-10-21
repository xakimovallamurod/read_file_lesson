
# 01
def read_file(filename):
    """
    Fayldagi vergul bilan ajratilgan sonlarni butun sonlar ro'yxati ko'rinishida qaytaring.

    Argumentlar:
        filename (str): fayl nomi

    Qaytaradi:
        list: sonlar
    """
    pass


# 02
def count_numbers(filename):
    """
    Faylda nechta son borligini qaytaring.

    Argumentlar:
        filename (str): fayl nomi

    Qaytaradi:
        int: sonlar soni
    """
    pass


# 03
def first_number(filename):
    """
    Birinchi kundagi qadamlar sonini qaytaring.

    Argumentlar:
        filename (str): fayl nomi

    Qaytaradi:
        int: son
    """
    pass


# 04
def last_number(filename):
    """
    Oxirgi kundagi qadamlar sonini qaytaring.

    Argumentlar:
        filename (str): fayl nomi

    Qaytaradi:
        int: son
    """
    pass


# 05
def sum_numbers(filename):
    """
    Barcha kunlardagi qadamlar yig'indisini qaytaring.

    Argumentlar:
        filename (str): fayl nomi

    Qaytaradi:
        int: yig'indi
    """
    pass


# 06
def max_number(filename):
    """
    Eng ko'p qadam tashlangan kundagi qadamlar sonini qaytaring.

    Argumentlar:
        filename (str): fayl nomi

    Qaytaradi:
        int: eng katta son
    """
    pass


# 07
def min_number(filename):
    """
    Eng kam qadam tashlangan kundagi qadamlar sonini qaytaring.

    Argumentlar:
        filename (str): fayl nomi

    Qaytaradi:
        int: eng kichik son
    """
    pass


# 08
def average(filename):
    """
    Kunlik o'rtacha qadamlar sonini 1 xona aniqlikda yaxlitlab qaytaring.

    Argumentlar:
        filename (str): fayl nomi

    Qaytaradi:
        float: o'rtacha
    """
    pass


# 09
def not_round_numbers(filename):
    """
    1000 ga qoldiqsiz bo'linmaydigan sonlarni ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        filename (str): fayl nomi

    Qaytaradi:
        list: sonlar
    """
    pass


# 10
def count_above(filename, chegara):
    """
    Chegara berilgan. Qadamlar soni chegaradan ko'p bo'lgan kunlar sonini qaytaring.

    Argumentlar:
        filename (str): fayl nomi
        chegara (int): chegara

    Qaytaradi:
        int: kunlar soni
    """
    pass


# 11
def sorted_numbers(filename):
    """
    Sonlarni o'sish tartibida saralab qaytaring.

    Argumentlar:
        filename (str): fayl nomi

    Qaytaradi:
        list: saralangan sonlar
    """
    pass


# 12
def top3(filename):
    """
    Eng ko'p qadam tashlangan 3 kunning qadamlarini kamayish tartibida qaytaring.

    Argumentlar:
        filename (str): fayl nomi

    Qaytaradi:
        list: 3 ta son
    """
    pass


# 13
def best_day(filename):
    """
    Eng ko'p qadam tashlangan kunning raqamini qaytaring (kunlar 1 dan boshlanadi; teng bo'lsa, birinchisi).

    Argumentlar:
        filename (str): fayl nomi

    Qaytaradi:
        int: kun raqami
    """
    pass


# 14
def goal_days(filename, maqsad):
    """
    Allamurodning kunlik maqsadi berilgan. Maqsadga erishilgan (qadamlar maqsaddan kam emas) kunlar raqamlarini ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        filename (str): fayl nomi
        maqsad (int): kunlik maqsad

    Qaytaradi:
        list: kun raqamlari
    """
    pass


# 15
def steps_range(filename):
    """
    Eng ko'p va eng kam qadamlar orasidagi farqni qaytaring.

    Argumentlar:
        filename (str): fayl nomi

    Qaytaradi:
        int: farq
    """
    pass


# 16
def daily_changes(filename):
    """
    Har bir kun oldingi kunga nisbatan qancha o'zgarganini ro'yxat ko'rinishida qaytaring (2-kundan boshlab: bugun − kecha).

    Argumentlar:
        filename (str): fayl nomi

    Qaytaradi:
        list: o'zgarishlar
    """
    pass


# 17
def cumulative(filename):
    """
    Har bir kun oxiriga qadar jami qadamlar sonini (yig'ilib boruvchi yig'indi) ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        filename (str): fayl nomi

    Qaytaradi:
        list: yig'ilgan qadamlar
    """
    pass


# 18
def longest_streak(filename, maqsad):
    """
    Kunlik maqsad berilgan. Maqsadga ketma-ket erishilgan eng uzun davr necha kundan iboratligini qaytaring.

    Argumentlar:
        filename (str): fayl nomi
        maqsad (int): kunlik maqsad

    Qaytaradi:
        int: kunlar soni
    """
    pass


# 19
def unique_sorted(filename):
    """
    Takrorlanuvchi sonlarni olib tashlab, qolganlarini o'sish tartibida qaytaring.

    Argumentlar:
        filename (str): fayl nomi

    Qaytaradi:
        list: sonlar
    """
    pass


# 20
def report(filename):
    """
    "Jami: <yig'indi> | O'rtacha: <o'rtacha> | Eng ko'p: <kun>-kun" ko'rinishidagi hisobot satrini qaytaring (o'rtacha 1 xona aniqlikda).

    Argumentlar:
        filename (str): fayl nomi

    Qaytaradi:
        str: hisobot
    """
    pass


# Tekshirish
print(read_file("data.txt"))
