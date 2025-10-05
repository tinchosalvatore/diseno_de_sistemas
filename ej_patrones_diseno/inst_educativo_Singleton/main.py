from instituto import InstitutoEducativo
import time

def main():
    instituto1 = InstitutoEducativo.get_instance()
    instituto2 = InstitutoEducativo.get_instance()

    print(f"Imprimiendo el ID de ambas instancias: {id(instituto1)} y {id(instituto2)}")
    print("Debido al uso de Singleton, deberia haber sido el mismo ID")

    print("Probando con un if si son el mismo....")
    
    time.sleep(2)
    if instituto1 is instituto2:
        print("Existe solo una instancia de InstitutoEducativo")

if __name__ == "__main__":
    main()