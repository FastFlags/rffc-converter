def sex(reallyrich, retardcr):
    rc = reallyrich / retardcr
    return rc

def main():
    retardcr = 142069
    while True:
        try:
            reallyrich_str = input("Enter the amount: ")
            if reallyrich_str.lower() == 'exit':
                break
            
            reallyrich = float(reallyrich_str)
            if reallyrich < 0:
                print("Please enter a valid number you dumb fuck.")
                continue
            elif reallyrich == 0:
                print("nigga is u fukin retarded ofc its 0 u dumb bitch")
                continue
            elif reallyrich > 0:
                rc = sex(reallyrich, retardcr)
                formatted_reallyrich = reallyrich_str if '.' in reallyrich_str else f"{int(reallyrich)}"
                print(f"{formatted_reallyrich} dollars is {rc:.5f} RC")
        except ValueError:
            print("Invalid input. Please enter a valid number you dumb fuck.")

if __name__ == "__main__":
    main()
