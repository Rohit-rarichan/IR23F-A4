# a4.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Rohit George Rarichan
# rraricha@uci.edu
# 36126645
from LastFM import FM_main
from OpenWeather import weather_main

if __name__ == '__main__':
    loop = 'Y'
    while loop != 'N':
        ans = input("Do you wish to use the Weather API or the LastFM API (type weather or FM)")
        if ans == "weather":
            weather_main()
        elif ans == "FM":
            FM_main()
        else:
            print("Invalid option")
        loop = input("Do you wish to continue Y/N: ")
