def check_vowels():
    # Código a implementar utilizando input.
    nombre= input()
    nombre= nombre.lower()
    a="a"
    e="e"
    i="i"
    o="o"
    u="u"
    print(f"Contiene a:{a in nombre}")
    print(f"Contiene e:{e in nombre}")
    print(f"Contiene i:{i in nombre}")
    print(f"Contiene o:{o in nombre}")
    print(f"Contiene u:{u in nombre}")

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
