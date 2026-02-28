{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def hitung_rata_rata(nilai):\
    total = 0\
    for n in nilai:\
       # total = n -> ini kode salah\
       total +=n\
    return total / len(nilai)\
\
def kategori_nilai(rata):\
    if rata >= 85:\
        return "A"\
    elif rata >= 75:\
        return "B"\
    elif rata >= 65:\
        return "C"\
    else:\
        return "D"\
\
data = [80, 90, 75]\
rata = hitung_rata_rata(data)\
\
print("Rata-rata:", rata)\
#print("Kategori:", kategori_nilai) -> tidak ada kategori nilai (rata)\
print("Kategori:", kategori_nilai(rata))\
}