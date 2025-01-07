import qrcode
import qrcode.constants

def generar_qr_wifi(ssid, password, tipo_seguridad="WPA2", nombre_archivo="wifi_qr.png"):
    """
    Genera un código QR para conectarse a una red Wi-Fi.

    Args:
        ssid: Nombre de la red (SSID).
        password: Contraseña de la red.
        tipo_seguridad: Tipo de seguridad (WPA/WPA2, WEP). Por defecto es WPA2.
        nombre_archivo: Nombre del archivo donde se guardará la imagen del QR.
    """

    data = {
        "S": ssid,
        "T": tipo_seguridad,
        "P": password
    }

    # Formato para la cadena de configuración Wi-Fi
    wifi_config = f"WIFI:S:{data['S']};T:{data['T']};P:{data['P']};;"

    qr = qrcode.QRCode(
        version=1,  # Ajustar si se necesita más capacidad
        error_correction=qrcode.constants.ERROR_CORRECT_L, # Nivel de corrección de errores (L, M, Q, H)
        box_size=10, # Tamaño de cada cuadro del QR
        border=4, # Margen del QR
    )

    qr.add_data(wifi_config)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nombre_archivo)

    print(f"Código QR guardado en {nombre_archivo}")

# Ejemplo de uso:
ssid = "NombreDeTuRed"  # Reemplaza con el nombre de tu red
password = "TuContraseña"  # Reemplaza con tu contraseña
tipo_seguridad = "WPA2" # Puedes cambiarlo a WEP si es necesario
nombre_archivo = "mi_wifi.png" #Nombre del archivo de la imagen

generar_qr_wifi(ssid, password, tipo_seguridad, nombre_archivo)


# Otro ejemplo de uso, usando valores por defecto:
generar_qr_wifi("OtraRed","OtraContraseña") # Guarda la imagen como wifi_qr.png