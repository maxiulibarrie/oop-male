from entities import Clothe, Shop

if __name__=="__main__":
    compra= Shop(fecha= "5/5/23")
    
    compra.add_clothe("remera", "roja", "s", 6000)
    compra.add_clothe("short", "amarillo", "m", 9000)
    compra.add_clothe("pañuelo", "verde", "s", 700) 
    
    print(f"El total es: {compra.get_total()}")