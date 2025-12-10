"""
Miniräknare med grundläggande matematiska operationer.

Skriven av Claude.AI den 10 december 2025

"""

class Kalkylator:
    """En enkel miniräknare som kan utföra grundläggande matematiska operationer."""
    
    def summa(self, a: float, b: float) -> float:
        """
        Beräknar summan av två tal.
        
        Args:
            a: Första talet
            b: Andra talet
            
        Returns:
            Summan av a och b
        """
        return a + b
    
    def differens(self, a: float, b: float) -> float:
        """
        Beräknar differensen mellan två tal.
        
        Args:
            a: Första talet
            b: Andra talet
            
        Returns:
            Differensen a - b
        """
        return a - b
    
    def produkt(self, a: float, b: float) -> float:
        """
        Beräknar produkten av två tal.
        
        Args:
            a: Första talet
            b: Andra talet
            
        Returns:
            Produkten a * b
        """
        return a * b
    
    def kvot(self, a: float, b: float) -> float:
        """
        Beräknar kvoten av två tal.
        
        Args:
            a: Täljare
            b: Nämnare
            
        Returns:
            Kvoten a / b
            
        Raises:
            ValueError: Om nämnaren är noll
        """
        if b == 0:
            raise ValueError("Division med noll är inte tillåten")
        return a / b


if __name__ == "__main__":
    # Exempel på användning
    kalk = Kalkylator()
    
    print("=== Kalkylator Demo ===")
    print(f"10 + 5 = {kalk.summa(10, 5)}")
    print(f"10 - 5 = {kalk.differens(10, 5)}")
    print(f"10 * 5 = {kalk.produkt(10, 5)}")
    print(f"10 / 5 = {kalk.kvot(10, 5)}")
    
    try:
        kalk.kvot(10, 0)
    except ValueError as e:
        print(f"Fel: {e}")
        