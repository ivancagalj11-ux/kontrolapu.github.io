import sys
print("--- Python Path ---")
for p in sys.path:
    print(p)
print("--------------------")

try:
    # Pokušaj importirati problematične klase
    from openpyxl.worksheet.header_footer import OddHeader, OddFooter
    print("\nSUCCESS: Uspješan import OddHeader i OddFooter!")

    # Provjeri verziju iz samog modula
    import openpyxl
    print(f"Verzija openpyxl koju Python koristi: {openpyxl.__version__}")
    print(f"Lokacija openpyxl modula: {openpyxl.__file__}")

except ImportError as e:
    print(f"\nERROR: Import nije uspio!")
    print(e)
    # Ispiši verziju ako je import samog openpyxl uspio
    try:
        import openpyxl
        print(f"(Verzija openpyxl koju Python koristi: {openpyxl.__version__})")
        print(f"(Lokacija openpyxl modula: {openpyxl.__file__})")
    except ImportError:
        print("(Nije moguće importirati ni osnovni openpyxl modul)")

except Exception as ex:
    print(f"\nUNEXPECTED ERROR: {ex}")