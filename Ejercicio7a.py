correo = input("Introduce tu correo eletrónico: " "\n")
correo_nuevo = correo[:correo.find("@")]+ "@ceu.es"
print(correo_nuevo)
