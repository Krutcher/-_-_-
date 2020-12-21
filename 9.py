ralph_waldo_emerson = """There are a number of traditions for weddings that have survived into the 21st century. It is still traditional for the bride and groom to have their own parties the night before getting married. The groom’s party is called a ‘Stag party’, while the bride’s is known as a ‘Hen party’.
On the morning of the wedding, the groom should not see the bride. If he does, this is bad luck. The bride puts on her special wedding dress, which is usually white. She also needs to wear ‘something old, something new, something borrowed and something blue’.
At the church, or registry office, the bride and groom exchange rings before walking together back down the aisle. When they get outside, the bride throws her bouquet in the air. Tradition says that whoever catches it will be the next person to get married.
But it’s not only the bride who throws something. All the people at the wedding throw confetti and rice over the happy couple.
Finally, after the reception, the bride and groom drive off to have their honeymoon.
"""
world_emerson = set(map(str.lower,ralph_waldo_emerson.split(' ')))
for i in world_emerson:
    i = i.strip('.,')
    n = ralph_waldo_emerson.count(i)
    print('Слово '+str(i)+' встречается '+str(n)+' раз')
