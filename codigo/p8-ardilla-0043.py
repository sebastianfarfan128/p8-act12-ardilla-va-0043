# Sebastian Farfan NC = 0043
import os
import cv2

# Obtener la ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Cargar la imagen usando la ruta correcta
ruta_entrada = os.path.join(BASE_DIR, "imagenes", "Ardilla.jpg")
imagen = cv2.imread(ruta_entrada)

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(
    imagen,
    5
)

# Mostrar imágenes
cv2.imshow("Ardilla original", imagen)
cv2.imshow("Ardilla con filtro de mediana", imagen_filtrada)

# Guardar resultado
ruta_salida = os.path.join(BASE_DIR, "resultados", "Ardilla_mediana.jpg")
cv2.imwrite(
    ruta_salida,
    imagen_filtrada
)

print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en:")
print(ruta_salida)

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print("Codigo hecho por Sebastian Farfan NC = 0043")