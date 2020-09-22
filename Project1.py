conditon = True
while conditon == True:
    print('''
        Zodiac signs
        Select a sign and your future will be predicted.
        1.Aries	
        2.Taurus	
        3.Gemini	
        4.Cancer	
        5.Leo	
        6.Virgo	
        7.Libra	
        8.Scorpio	
        9.Sagittarius	
        10.Capricorn	
        11.Aquarius
        12.Pisces
      ''')

    z = int(input("Enter the zodiac number according to the list:"))
    if z == 1:
        print('''
        Aries: The pioneer and trailblazer of the horoscope wheel, Aries energy helps us initiate, fight for our beliefs and fearlessly put ourselves out there.''')

    elif z == 2:
        print('''
        Taurus:The persistent provider of the horoscope family, Taurus energy helps us seek security, enjoy earthly pleasures and get the job done.
        ''')
    elif z == 3:
        print('''
        Gemini:The most versatile and vibrant horoscope sign, Gemini energy helps us communicate, collaborate and fly our freak flags at full mast''')
    elif z == 4:
        print('''
        Cancer:The natural nurturer of the horoscope wheel, Cancer energy helps us connect with our feelings, plant deep roots and feather our family nests.
       ''')
    elif z == 5:
        print('''
        Leo:The drama and regal ruler of the horoscope clan, Leo energy helps us shine, express ourselves boldly and wear our hearts on our sleeves.
        ''')
    elif z == 6:
        print('''
        Virgo:The masterful helper of the horoscope wheel, Virgo energy teaches us to serve, do impeccable work and prioritize wellbeing of ourselves, our loved ones and the planet
        ''')
    elif z == 7:
        print('''
        Libra:The balance of the horoscope family, Libra energy inspires us to seek peace, harmony and cooperation and to do it with style and grace
       ''')
    elif z == 8:
        print('''
        Scorpio:The most intense and focused of the horoscope signs, Scorpio energy helps us dive deep, merge our superpowers and form bonds that are built to last
        ''')
    elif z == 9:
        print('''
        Sagittarius:The wordly adventurer of the horoscope wheel, Sagittarius energy inspires us to dream big, chase the impossible and take fearless risks
       ''')
    elif z == 10:
       print('''
       Capricorn:
       The measured master planner of the horoscope family, Capricon energy teaches us the power of structure and long-term goals.''')
    elif z == 11:
        print('''
        Aquarius:The mad scientist and humanitarian of the horoscope wheel, futuristic Aquarius helps us innovate and unite for social justice
        ''')
    elif z == 12:
        print('''
        Pisces:The dreamer and healer of the horoscope family, Pisces energy awakens compassion, imagination and artistry, uniting us as one
        !!!!!!!''')

    conditon = True if input(" \n \n Do you want to try again? (Y/N): ") == 'Y' else print("THANKYOU")
