def centrar(ventana, ancho_app, largo_app):
    width_sc = ventana.winfo_screenwidth()
    height_sc = ventana.winfo_screenheight()
    x = int((width_sc/2) - (ancho_app/2))
    y = int((height_sc/2) - (largo_app/2))
    return ventana.geometry(f"{ancho_app}x{largo_app}+{x}+{y}")