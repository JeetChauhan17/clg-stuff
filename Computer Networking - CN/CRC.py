def xor(check, polynomial):
    result = []
    for i in range(len(polynomial)):
        result.append('0' if check[i] == polynomial[i] else '1')
    return ''.join(result)


def crc(data, polynomial):
    n = len(polynomial) 
    padded_data = data + '0' * (n - 1)  
    check = list(padded_data) 
    for i in range(len(data)):
        if check[i] == '1':  
            check[i:i + n] = xor(check[i:i + n], polynomial)
    return ''.join(check[-(n - 1):])


def receiver(data, polynomial):
    print("Data received:", data)
    crcvalue = crc(data[:-len(polynomial) + 1], polynomial)  
    if '1' in crcvalue:
        print("NO Error detected\n")
    else:
        print("error detected\n")


def main():
    data = input("Enter data :")
    polynomial = input("Enter the polynomial: ")
    crcvalue = crc(data, polynomial)
    final_data = data + crcvalue
    print("CRC value is:", crcvalue)
    print("Final data to be sent:", final_data)
    

    receiver(final_data, polynomial)


if __name__ == "__main__":
    main()
