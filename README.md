# Fayldan o'qish

`data.txt` faylida Allamurodning 10 kunlik qadamlari soni vergul bilan ajratib yozilgan. Barcha funksiyalar `main.py` faylida va fayl nomini qabul qiladi.

## 01. read_file

Fayldagi vergul bilan ajratilgan sonlarni butun sonlar ro'yxati ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: filename="data.txt"
Chiqarish: [8000, 12000, 10000, 13000, 11000, 7000, 13000, 9500, 10500, 12500]
```

---

## 02. count_numbers

Faylda nechta son borligini qaytaring.

**Misol 1:**

```Python
Kirish: filename="data.txt"
Chiqarish: 10
```

---

## 03. first_number

Birinchi kundagi qadamlar sonini qaytaring.

**Misol 1:**

```Python
Kirish: filename="data.txt"
Chiqarish: 8000
```

---

## 04. last_number

Oxirgi kundagi qadamlar sonini qaytaring.

**Misol 1:**

```Python
Kirish: filename="data.txt"
Chiqarish: 12500
```

---

## 05. sum_numbers

Barcha kunlardagi qadamlar yig'indisini qaytaring.

**Misol 1:**

```Python
Kirish: filename="data.txt"
Chiqarish: 106500
```

---

## 06. max_number

Eng ko'p qadam tashlangan kundagi qadamlar sonini qaytaring.

**Misol 1:**

```Python
Kirish: filename="data.txt"
Chiqarish: 13000
```

---

## 07. min_number

Eng kam qadam tashlangan kundagi qadamlar sonini qaytaring.

**Misol 1:**

```Python
Kirish: filename="data.txt"
Chiqarish: 7000
```

---

## 08. average

Kunlik o'rtacha qadamlar sonini 1 xona aniqlikda yaxlitlab qaytaring.

**Misol 1:**

```Python
Kirish: filename="data.txt"
Chiqarish: 10650.0
```

---

## 09. not_round_numbers

1000 ga qoldiqsiz bo'linmaydigan sonlarni ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: filename="data.txt"
Chiqarish: [9500, 10500, 12500]
```

---

## 10. count_above

Chegara berilgan. Qadamlar soni chegaradan ko'p bo'lgan kunlar sonini qaytaring.

**Misol 1:**

```Python
Kirish: filename="data.txt", chegara=10000
Chiqarish: 6
```

**Misol 2:**

```Python
Kirish: filename="data.txt", chegara=15000
Chiqarish: 0
```

---

## 11. sorted_numbers

Sonlarni o'sish tartibida saralab qaytaring.

**Misol 1:**

```Python
Kirish: filename="data.txt"
Chiqarish: [7000, 8000, 9500, 10000, 10500, 11000, 12000, 12500, 13000, 13000]
```

---

## 12. top3

Eng ko'p qadam tashlangan 3 kunning qadamlarini kamayish tartibida qaytaring.

**Misol 1:**

```Python
Kirish: filename="data.txt"
Chiqarish: [13000, 13000, 12500]
```

---

## 13. best_day

Eng ko'p qadam tashlangan kunning raqamini qaytaring (kunlar 1 dan boshlanadi; teng bo'lsa, birinchisi).

**Misol 1:**

```Python
Kirish: filename="data.txt"
Chiqarish: 4
```

---

## 14. goal_days

Allamurodning kunlik maqsadi berilgan. Maqsadga erishilgan (qadamlar maqsaddan kam emas) kunlar raqamlarini ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: filename="data.txt", maqsad=12000
Chiqarish: [2, 4, 7, 10]
```

---

## 15. steps_range

Eng ko'p va eng kam qadamlar orasidagi farqni qaytaring.

**Misol 1:**

```Python
Kirish: filename="data.txt"
Chiqarish: 6000
```

---

## 16. daily_changes

Har bir kun oldingi kunga nisbatan qancha o'zgarganini ro'yxat ko'rinishida qaytaring (2-kundan boshlab: bugun − kecha).

**Misol 1:**

```Python
Kirish: filename="data.txt"
Chiqarish: [4000, -2000, 3000, -2000, -4000, 6000, -3500, 1000, 2000]
```

---

## 17. cumulative

Har bir kun oxiriga qadar jami qadamlar sonini (yig'ilib boruvchi yig'indi) ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: filename="data.txt"
Chiqarish: [8000, 20000, 30000, 43000, 54000, 61000, 74000, 83500, 94000, 106500]
```

---

## 18. longest_streak

Kunlik maqsad berilgan. Maqsadga ketma-ket erishilgan eng uzun davr necha kundan iboratligini qaytaring.

**Misol 1:**

```Python
Kirish: filename="data.txt", maqsad=10000
Chiqarish: 4
```

**Misol 2:**

```Python
Kirish: filename="data.txt", maqsad=20000
Chiqarish: 0
```

---

## 19. unique_sorted

Takrorlanuvchi sonlarni olib tashlab, qolganlarini o'sish tartibida qaytaring.

**Misol 1:**

```Python
Kirish: filename="data.txt"
Chiqarish: [7000, 8000, 9500, 10000, 10500, 11000, 12000, 12500, 13000]
```

---

## 20. report

"Jami: <yig'indi> | O'rtacha: <o'rtacha> | Eng ko'p: <kun>-kun" ko'rinishidagi hisobot satrini qaytaring (o'rtacha 1 xona aniqlikda).

**Misol 1:**

```Python
Kirish: filename="data.txt"
Chiqarish: "Jami: 106500 | O'rtacha: 10650.0 | Eng ko'p: 4-kun"
```

