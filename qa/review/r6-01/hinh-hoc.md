# R6-01 · So hình học trang con: build PR với build gốc 3131e7e

Công cụ: `qa/r6geo.js` (đo), `qa/r6geocmp.py` (so, sai số 2px), `qa/r6herotable.py` (bảng hero), `qa/r6contrastcmp.py` (tương phản).
Đo 19 trang con (trừ trang chủ), VI, ở 1440, 1024, 390; EN và 768 kiểm mẫu. Mỗi khối cấp 1 của `<main>` và thanh mục con: vị trí, cao, rộng, padding, margin; mỗi dòng chữ: toạ độ trong khối, rộng, cao, cỡ chữ, line-height, giãn chữ; ảnh: vị trí, kích thước.

## Cách đọc

Ba build: **gốc** (3131e7e), **đối chứng** (3131e7e cộng đúng các sửa phải giữ: chữ Hán R4-05, tắt script ép chữ, căn trái, text-wrap; dựng ngoài repo, không có thay đổi hình học nào khác), **PR**.
So PR với đối chứng: chỉ còn các khung ảnh hero (màu A). So PR với gốc: thêm các chỗ do sửa phải giữ.

## Chiều cao hero (px, VI)

| Rộng | Trang | Gốc 3131e7e | main | PR |
|---|---|---|---|---|
| 1440 | about | 775 | 564 | 775 |
| 1440 | phvsf | 775 | 600 | 775 |
| 1440 | vnshine | 775 | 600 | 775 |
| 1440 | member | 795 | 625 | 795 |
| 1440 | portfolio | 795 | 625 | 795 |
| 1440 | advisory | 795 | 625 | 795 |
| 1440 | academy | 775 | 560 | 775 |
| 1440 | careers | 775 | 625 | 775 |
| 1440 | guidePhvsf | 345 | 401 | 345 |
| 1440 | guideVnshine | 327 | 383 | 327 |
| 1024 | about | 952 | 939 | 951 |
| 1024 | phvsf | 803 | 865 | 803 |
| 1024 | vnshine | 844 | 920 | 844 |
| 1024 | member | 803 | 596 | 803 |
| 1024 | portfolio | 803 | 545 | 803 |
| 1024 | advisory | 803 | 537 | 803 |
| 1024 | academy | 915 | 915 | 915 |
| 1024 | careers | 803 | 537 | 803 |
| 1024 | guidePhvsf | 345 | 401 | 345 |
| 1024 | guideVnshine | 383 | 383 | 383 |
| 390 | about | 944 | 777 | 943 |
| 390 | phvsf | 996 | 1014 | 996 |
| 390 | vnshine | 1197 | 1113 | 1197 |
| 390 | member | 1169 | 810 | 1169 |
| 390 | portfolio | 1087 | 728 | 1087 |
| 390 | advisory | 1056 | 696 | 1056 |
| 390 | academy | 803 | 599 | 803 |
| 390 | careers | 803 | 641 | 803 |
| 390 | guidePhvsf | 468 | 468 | 468 |
| 390 | guideVnshine | 489 | 489 | 489 |

## PR so với đối chứng (sai số 2px): chỉ còn khung ảnh hero của màu A

```
about vi 1440          7 lệch: khung trong y 1, khung trong h 1, khung trong w 1, ảnh dx 1, ảnh dy 1, ảnh w 1, ảnh h 1
       khung trong y | ab-overview y: 0 -> 56
       khung trong h | ab-overview h: 774 -> 663
       khung trong w | ab-overview w: 1036.8 -> 560
       ảnh dx | ab-overview|img|0: 403.2 -> 752
       ảnh dy | ab-overview|img|0: 0 -> 56
       ảnh w | ab-overview|img|0: 1036.8 -> 560
       ảnh h | ab-overview|img|0: 774 -> 663
academy vi 1440        7 lệch: khung trong y 1, khung trong h 1, khung trong w 1, ảnh dx 1, ảnh dy 1, ảnh w 1, ảnh h 1
       khung trong y | dh y: 0 -> 56
       khung trong h | dh h: 775 -> 663
       khung trong w | dh w: 1036.8 -> 560
       ảnh dx | b0|img|0: 403.2 -> 752
       ảnh dy | b0|img|0: 0 -> 56
       ảnh w | b0|img|0: 1036.8 -> 560
       ảnh h | b0|img|0: 775 -> 663
about vi 1024          4 lệch: ảnh dx 1, ảnh dy 1, ảnh w 1, ảnh h 1
       ảnh dx | ab-overview|img|0: 0 -> 16
       ảnh dy | ab-overview|img|0: 531 -> 575
       ảnh w | ab-overview|img|0: 1024 -> 992
       ảnh h | ab-overview|img|0: 420 -> 340
phvsf vi 1024          2 lệch: ảnh dy 1, ảnh h 1
       ảnh dy | b0|img|0: 0 -> 390
       ảnh h | b0|img|0: 803 -> 534
vnshine vi 1024        2 lệch: ảnh dy 1, ảnh h 1
       ảnh dy | b0|img|0: 0 -> 437.9
       ảnh h | b0|img|0: 843.9 -> 534
about vi 390           4 lệch: ảnh dx 1, ảnh dy 1, ảnh w 1, ảnh h 1
       ảnh dx | ab-overview|img|0: 0 -> 16
       ảnh dy | ab-overview|img|0: 522.9 -> 566.9
       ảnh w | ab-overview|img|0: 390 -> 358
       ảnh h | ab-overview|img|0: 420 -> 340
phvsf vi 390           2 lệch: ảnh dy 1, ảnh h 1
       ảnh dy | b0|img|0: 0 -> 481.8
       ảnh h | b0|img|0: 995.8 -> 642
vnshine vi 390         2 lệch: ảnh dy 1, ảnh h 1
       ảnh dy | b0|img|0: 0 -> 577.8
       ảnh h | b0|img|0: 1196.8 -> 747
Tổng lệch: 30 trên 57 lượt trang
```

## PR so với gốc (sai số 2px), số lượng theo trang

```
about vi 1440          51 lệch: khung trong y 1, khung trong h 2, khung trong w 1, khối h 2, khối y 6, chữ thừa ở PR 1, chữ rộng 7, giãn chữ 1, chữ cao 1, chữ y 24, ảnh dx 1, ảnh dy 1, ảnh w 1, ảnh h 1, cao trang 1
funds vi 1440          OK
phvsf vi 1440          4 lệch: chữ rộng 3, giãn chữ 1
vnshine vi 1440        42 lệch: khối h 1, khung trong h 1, khối y 7, chữ rộng 8, giãn chữ 2, chữ cao 1, chữ y 21, cao trang 1
member vi 1440         7 lệch: chữ y 4, chữ rộng 2, chữ cao 1
portfolio vi 1440      5 lệch: chữ y 3, chữ rộng 1, chữ cao 1
advisory vi 1440       1 lệch: chữ rộng 1
ir vi 1440             OK
news vi 1440           10 lệch: chữ rộng 9, giãn chữ 1
academy vi 1440        10 lệch: khung trong y 1, khung trong h 1, khung trong w 1, chữ rộng 3, ảnh dx 1, ảnh dy 1, ảnh w 1, ảnh h 1
careers vi 1440        7 lệch: chữ y 4, chữ rộng 2, chữ cao 1
contact vi 1440        OK
guidePhvsf vi 1440     2 lệch: chữ rộng 2
guideVnshine vi 1440   70 lệch: khối h 2, khối y 2, khung trong h 1, giãn chữ 1, chữ cao 2, chữ y 52, chữ rộng 2, ảnh dy 7, cao trang 1
faq vi 1440            1 lệch: chữ rộng 1
glossary vi 1440       16 lệch: chữ rộng 15, giãn chữ 1
forms vi 1440          OK
terms vi 1440          5 lệch: chữ rộng 5
privacy vi 1440        4 lệch: chữ rộng 4
about vi 1024          46 lệch: khối h 2, khung trong h 1, khối y 6, chữ thừa ở PR 1, chữ rộng 5, giãn chữ 1, chữ cao 1, chữ y 24, ảnh dx 1, ảnh dy 1, ảnh w 1, ảnh h 1, cao trang 1
funds vi 1024          OK
phvsf vi 1024          8 lệch: chữ rộng 5, giãn chữ 1, ảnh dy 1, ảnh h 1
vnshine vi 1024        10 lệch: giãn chữ 1, chữ rộng 7, ảnh dy 1, ảnh h 1
member vi 1024         3 lệch: giãn chữ 1, chữ rộng 2
portfolio vi 1024      2 lệch: giãn chữ 1, chữ rộng 1
advisory vi 1024       2 lệch: giãn chữ 1, chữ rộng 1
ir vi 1024             OK
news vi 1024           11 lệch: chữ rộng 11
academy vi 1024        1 lệch: chữ rộng 1
careers vi 1024        2 lệch: chữ rộng 2
contact vi 1024        OK
guidePhvsf vi 1024     4 lệch: giãn chữ 1, chữ rộng 3
guideVnshine vi 1024   10 lệch: khối h 1, khung trong h 1, chữ rộng 3, chữ cao 1, chữ y 3, cao trang 1
faq vi 1024            2 lệch: chữ rộng 2
glossary vi 1024       3 lệch: chữ rộng 3
forms vi 1024          OK
terms vi 1024          5 lệch: chữ rộng 5
privacy vi 1024        4 lệch: chữ rộng 4
about vi 390           41 lệch: khối h 1, khối y 3, chữ thừa ở PR 1, chữ rộng 5, chữ x 12, chữ y 12, chữ cao 2, ảnh dx 1, ảnh dy 1, ảnh w 1, ảnh h 1, cao trang 1
funds vi 390           1 lệch: chữ rộng 1
phvsf vi 390           4 lệch: giãn chữ 1, chữ rộng 1, ảnh dy 1, ảnh h 1
vnshine vi 390         4 lệch: chữ rộng 2, ảnh dy 1, ảnh h 1
member vi 390          OK
portfolio vi 390       OK
advisory vi 390        OK
ir vi 390              OK
news vi 390            11 lệch: chữ rộng 11
academy vi 390         1 lệch: chữ rộng 1
careers vi 390         2 lệch: chữ rộng 2
contact vi 390         OK
guidePhvsf vi 390      2 lệch: chữ rộng 2
guideVnshine vi 390    1 lệch: chữ rộng 1
faq vi 390             2 lệch: chữ rộng 2
glossary vi 390        10 lệch: chữ rộng 10
forms vi 390           OK
terms vi 390           OK
privacy vi 390         OK
Tổng lệch: 427 trên 57 lượt trang
```
