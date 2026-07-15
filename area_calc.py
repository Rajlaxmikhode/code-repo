def calculate_area(length, width):
    area=length*width
    return area
    
    
def main():
    length, width = map(int, input().split())
    area = calculate_area(length, width)
    print(area)


main()
