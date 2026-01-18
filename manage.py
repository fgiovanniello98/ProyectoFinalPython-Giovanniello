#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "configuracion.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Activaste el entorno vi.venv\Scripts\activatertual e instalaste requirements?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
