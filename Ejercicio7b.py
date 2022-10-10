correo = input("Introduce tu correo eletrónico: " "\n")
correo_nuevo = correo[:correo.find("@")]+ "@ceu.es"
cadena = correo.split("@")
print(cadena[0],"usuario")
print(cadena[1],"correo")
print(correo_nuevo)
