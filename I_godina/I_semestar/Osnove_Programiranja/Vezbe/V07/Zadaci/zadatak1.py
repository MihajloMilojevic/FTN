
def subjective(temperature, wind):
    return 3.74+0.6215*temperature-35.75*(wind**0.16)+0.4275*temperature*(wind ** 0.16)

def create_table(wind_start, wind_end, temp_start, temp_end):
    def format_cell(string = ""):
        return string.ljust(10) + " "
    def header():
        string = format_cell()
        i = temp_start
        while(i <= temp_end):
            string += format_cell(f"t={i}")
            i += 1 
        return string
    def create_row(wind):
        string = format_cell(f"v={wind}")
        temp = temp_start
        while(temp <= temp_end):
            string += format_cell(f"{subjective(temp, wind):+.3f}")
            temp += 1 
        return string
    
    print(header())
    wind = wind_start
    while(wind <= wind_end):
        print(create_row(wind))
        wind += 1


def main():
    create_table(0, 10, 5, 10)


if __name__ == "__main__":
    main()