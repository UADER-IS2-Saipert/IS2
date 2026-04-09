import subprocess
import math

def run_rpn(expr):
    """Ejecuta rpn.py como CLI y devuelve float"""
    result=subprocess.run(
        ["python","rpn.py"]+expr.split(),
        capture_output=True,text=True
    )
    try:
        return float(result.stdout.strip())
    except ValueError:
        raise Exception(f"Salida inválida: {result.stdout.strip()}")

if __name__=="__main__":
    # ---------- Casos de prueba ----------
    # Suma
    assert run_rpn("5 3 +")==8.0
    # Resta
    assert run_rpn("10 4 -")==6.0
    # Multiplicación
    assert run_rpn("5 3 *")==15.0
    # División
    assert math.isclose(run_rpn("5 2 /"),2.5)
    # Constantes
    assert run_rpn("p e +")>5
    # Potencia
    assert run_rpn("2 3 yx")==8.0
    # Inverso
    assert run_rpn("4 1/x")==0.25
    # Memoria
    assert run_rpn("5 STO 00 RCL 00")==5.0
    # CHS
    assert run_rpn("5 chs")==-5.0
    # Dup + suma
    assert run_rpn("5 dup +")==10.0

    print("Todos los tests funcionales pasaron ✅")