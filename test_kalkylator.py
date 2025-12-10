"""
Pytest-tester för Miniräknare-klassen.

Skriven av Claude.AI den 10 december 2025

För att köra testerna:
    pytest test_kalkylator.py

För att köra med täckningsrapport:
    pytest --cov=kalkylator test_kalkylator.py
"""

import pytest
from kalkylator import kalkylator


@pytest.fixture
def kalk():
    """Fixture som skapar en ny miniräknare för varje test."""
    return kalkylator()


class TestSumma:
    """Tester för summa-funktionen."""
    
    def test_summa_positiva_tal(self, kalk):
        assert kalk.summa(5, 3) == 8
        assert kalk.summa(10, 20) == 30
    
    def test_summa_negativa_tal(self, kalk):
        assert kalk.summa(-5, -3) == -8
        assert kalk.summa(-10, -20) == -30
    
    def test_summa_blandade_tal(self, kalk):
        assert kalk.summa(5, -3) == 2
        assert kalk.summa(-10, 20) == 10
    
    def test_summa_med_noll(self, kalk):
        assert kalk.summa(0, 5) == 5
        assert kalk.summa(5, 0) == 5
    
    def test_summa_decimaler(self, kalk):
        assert kalk.summa(1.5, 2.3) == pytest.approx(3.8)
        assert kalk.summa(0.1, 0.2) == pytest.approx(0.3)


class TestDifferens:
    """Tester för differens-funktionen."""
    
    def test_differens_positiva_tal(self, kalk):
        assert kalk.differens(10, 5) == 5
        assert kalk.differens(20, 8) == 12
    
    def test_differens_negativa_tal(self, kalk):
        assert kalk.differens(-5, -3) == -2
        assert kalk.differens(-10, -20) == 10
    
    def test_differens_blandade_tal(self, kalk):
        assert kalk.differens(5, -3) == 8
        assert kalk.differens(-10, 5) == -15
    
    def test_differens_med_noll(self, kalk):
        assert kalk.differens(5, 0) == 5
        assert kalk.differens(0, 5) == -5
    
    def test_differens_decimaler(self, kalk):
        assert kalk.differens(5.5, 2.3) == pytest.approx(3.2)


class TestProdukt:
    """Tester för produkt-funktionen."""
    
    def test_produkt_positiva_tal(self, kalk):
        assert kalk.produkt(5, 3) == 15
        assert kalk.produkt(10, 10) == 100
    
    def test_produkt_negativa_tal(self, kalk):
        assert kalk.produkt(-5, -3) == 15
        assert kalk.produkt(-10, -2) == 20
    
    def test_produkt_blandade_tal(self, kalk):
        assert kalk.produkt(5, -3) == -15
        assert kalk.produkt(-10, 5) == -50
    
    def test_produkt_med_noll(self, kalk):
        assert kalk.produkt(0, 5) == 0
        assert kalk.produkt(5, 0) == 0
    
    def test_produkt_decimaler(self, kalk):
        assert kalk.produkt(2.5, 4) == 10.0
        assert kalk.produkt(1.5, 2.5) == pytest.approx(3.75)


class TestKvot:
    """Tester för kvot-funktionen."""
    
    def test_kvot_positiva_tal(self, kalk):
        assert kalk.kvot(10, 2) == 5
        assert kalk.kvot(15, 3) == 5
    
    def test_kvot_negativa_tal(self, kalk):
        assert kalk.kvot(-10, -2) == 5
        assert kalk.kvot(-15, -3) == 5
    
    def test_kvot_blandade_tal(self, kalk):
        assert kalk.kvot(10, -2) == -5
        assert kalk.kvot(-15, 3) == -5
    
    def test_kvot_decimaler(self, kalk):
        assert kalk.kvot(5, 2) == 2.5
        assert kalk.kvot(7.5, 2.5) == 3.0
    
    def test_kvot_med_noll_täljare(self, kalk):
        assert kalk.kvot(0, 5) == 0
    
    def test_kvot_med_noll_nämnare(self, kalk):
        with pytest.raises(ValueError, match="Division med noll är inte tillåten"):
            kalk.kvot(10, 0)
    
    def test_kvot_med_noll_bägge(self, kalk):
        with pytest.raises(ValueError, match="Division med noll är inte tillåten"):
            kalk.kvot(0, 0)


class TestIntegration:
    """Integrationstester som kombinerar flera operationer."""
    
    def test_kedjade_operationer(self, kalk):
        # (10 + 5) * 2 / 3 - 1
        resultat = kalk.summa(10, 5)
        resultat = kalk.produkt(resultat, 2)
        resultat = kalk.kvot(resultat, 3)
        resultat = kalk.differens(resultat, 1)
        assert resultat == pytest.approx(9.0)
    
    def test_komplexa_beräkningar(self, kalk):
        # (20 - 5) / (3 + 2)
        täljare = kalk.differens(20, 5)
        nämnare = kalk.summa(3, 2)
        resultat = kalk.kvot(täljare, nämnare)
        assert resultat == 3.0

        