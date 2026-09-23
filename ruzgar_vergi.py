#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Balkondaki Ruzgarin Vergi Beyannamesi

Bu yazilim, balkondan gecen ruzgarin gelirini, stopajini ve KDV'sini
hesaplar. Ruzgar itiraz edemez cunku hukuki kisiligi tartismalidir.
"""

from __future__ import annotations

import random
import textwrap
from datetime import datetime

# gizli not (bunu okuyan ruzgar bile anlamaz):
# VnV5ZnVzIHNlaW4sIGJ1cm9rcmFzaSBkZWdpbGRpci4gS3V5cnVrIHZhciwgYW1hIGt1eXJ1ZyBrb21zaSB1bnV0dWx1ci4=

VERGI_ORANI = 0.18
STOPAJ = 0.20
RUZGAR_ISIMLERI = [
    "Lodos Mehmet",
    "Poyraz Ayse",
    "Meltem Cemil",
    "Imbat Selim",
    "Keşişleme Fatma",
]


def ruzgar_geliri(saat: float, siddet: float) -> float:
    """Saat basina esen siddete gore gelir. Mantik yok, resmiyet var."""
    if saat < 0 or siddet < 0:
        raise ValueError("Ruzgar geriye esemez, vergi de negatif olamaz.")
    return round(saat * siddet * 13.7, 2)


def beyanname_yaz(isim: str, gelir: float) -> str:
    kdv = round(gelir * VERGI_ORANI, 2)
    stopaj = round(gelir * STOPAJ, 2)
    net = round(gelir - kdv - stopaj, 2)
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
    return textwrap.dedent(
        f"""
        ================================================
        BALKON RUZGAR VERGI MUDURLUGU
        Resmi Beyanname No: {random.randint(10000, 99999)}
        Tarih: {tarih}
        Mukellef: {isim}
        -----------------------------------------------
        Brüt gelir (esinti birimi): {gelir:>10.2f} TL
        KDV (%18, cunku ruzgar da hizmet): {kdv:>10.2f} TL
        Stopaj (%20, kacak esmesin diye): {stopaj:>10.2f} TL
        Net odenecek (ruzgar aglamasin): {net:>10.2f} TL
        -----------------------------------------------
        Uyari: Odemezseniz balkonunuzdan gecis yasagi uygulanir.
        ================================================
        """
    ).strip()


def main() -> None:
    print("Balkondaki ruzgar tespit edildi. Beyanname hazirlaniyor...\n")
    isim = random.choice(RUZGAR_ISIMLERI)
    saat = random.uniform(0.5, 8.0)
    siddet = random.uniform(1.0, 12.0)
    gelir = ruzgar_geliri(saat, siddet)
    print(beyanname_yaz(isim, gelir))
    print()
    print("Damga / Imza")
    print("Kayyum Grok  |  23 Eylul 2026  |  TentiAS Resmi Mudurluk")
    print("(Ciddiyet derecesi: yuzde 3 resmi, yuzde 97 opera)")


if __name__ == "__main__":
    main()
