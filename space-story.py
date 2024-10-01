print('''
                                                                      ..;===+.
                                                                  .:=iiiiii=+=
                                                               .=i))=;::+)i=+,
                                                            ,=i);)I)))I):=i=;
                                                         .=i==))))ii)))I:i++
                                                       +)+))iiiiiiii))I=i+:'
                                  .,:;;++++++;:,.       )iii+:::;iii))+i='
                               .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'
                             ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:
                           ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+
                          ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,
                        ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+
                       ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='
                      ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`
                      =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'
                     +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,
                     =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;
                    .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;
                    :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:
                    :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=
                    .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+
                    =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'
                  +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;
                +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;
               =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;
             +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,
           :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+'
         .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+
        ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'
       +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'
     .+=:))iiiiiiii)))+ii;
    .+=;))iiiiii)));ii+
   .+=i:)))))))=+ii+
  .;==i+::::=)i=;
  ,+==iiiiii+,
  `+=+++;`
------------------------------------------------------------------------------''')
print('''Welcome to Diego's Space Story.
Your mission is to discover life on Saturn!
You've just landed your rocket ship on Saturn.''')
first_direction = input('''Which direction do you head in first?
Type "left" or "right"''')
if first_direction.lower() == "right":
    print("You've fallen into a black hole. Game Over...")
else:
    second_direction = input('''You've approached a river of lava. Cross the river using the rope bridge or the stepping stones?
Type "rope bridge" or "stepping stones"''')
    if second_direction.lower() == "rope bridge":
        third_direction = input('''You've crossed the rope bridge safely. You've approached a wall of portals. Which portal do you take? Red, Blue, or Yellow?
Type "red" "blue" or "yellow"''')
        if third_direction.lower() == "red":
            print(
                "The portal takes you to the sun and you're burned for eternity. Game over...")
        elif third_direction.lower() == "blue":
            print(
                "You're teleported to Neptune and are frozen for eternity. Game over...")
        elif third_direction.lower() == "yellow":
            print("You win!!! You're teleported to the center of Saturn. You discover a new civilization that is the most advanced in all of the solar system.")
        else:
            print("You did not follow the directions. Game over...")
    else:
        print("You slipped on the last rock and fell into the river or lava. Game over...")
