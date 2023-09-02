## index(0) represents the name of weapon or sheild
## index(1) represents the energy of weapon or sheild
## index(2) represents the damage for weapon or save for sheild

class GRU :
## identifying class called GRU to store data of gru (weapons,sheilds,energy and health)

   G_ENERGY = 500
   G_HEALTH = 100
   G_weapons = [['FreezeGun', 50 ,11,'Inf'],['ElectricProd', 88, 18, 5],['Mega Magnet',92, 10,3],['KalmanMissile', 120 ,20 , 1]]
   G_Sheilds = [['Energy-Projected BarrierGun' ,20, 0.4 , 'Inf'],['Selective Permeability', 50 , 0.9 , 2]]
   
   
## method to see if gru is gonna choose weapon or sheild 
## GRU_weapon is storing the data of weapon or sheild which gru has chosen
   def GRU_choosing (G_weapons, G_Sheilds):

        GRU_choose =  input("GRU choose your weapon/sheild:" )
        if GRU_choose == 'weapon':
           GRU_weaponname = input("choose your weapon name: ")
           for i in range (4):
               if  GRU_weaponname == G_weapons[i][0]:
                   GRU_weapon = G_weapons[i]
                   print(GRU_weapon)
                   ## break statment is used the break the loop once we find the index of gru weapons matches with which he choose
                   return GRU_weapon,GRU_choose
                   break
        else:
           GRU_sheildname = input("choose your sheild name: ")
           for c in range (2):
              if  GRU_sheildname == G_Sheilds[c][0]:
                  GRU_sheild = G_Sheilds[c]
                  return  GRU_sheild,GRU_choose
                  break
 ## GRU_source stores the data of what gru chose 
 # GRU_choose stores either weapon or sheild         
   GRU_source,GRU_choose= GRU_choosing(G_weapons,G_Sheilds)

class VECTOR :
    ## here identifying VECTOR  class storing the weapons sheilds , energy and his health
    V_ENERGY = 500
    V_HEALTH = 100
    V_weapons = [['Laser Blasters', 40, 8, 'Inf'],['Plasma Grenades', 56, 13 ,8],['Sonic Resonance Cannon',100, 22, 3]]
    V_Sheilds = [['Energy Net Trap', 15, 0.23, 'Inf'],['Quantum Deflector',40, 0.8,3]]
    ## method to see if vector is gonna choose weapon or sheild 
    def choosing(V_weapons, V_Sheilds ):
        Vector_choose =  input("Vector choose your weapon/sheild:" )
        if Vector_choose == 'weapon':
            Vector_weaponname = input("choose your weapon name: ")
            for x in range (4):
              if  Vector_weaponname == V_weapons[x][0]:
                 V_weapon = V_weapons[x]
                 ## break statment is used the break the loop once we find the index of vector weapons matches with which he choose
                 return V_weapon,Vector_choose
                 break
               
        else:
          Vector_sheildname = input("choose your sheild name: ")
          ## for loop to search for what vector has chosen and store the data (if he chose weapon or sheild) in an array
          for y in range (2):
             if  Vector_sheildname == V_Sheilds[y][0]:
                 V_sheild = V_Sheilds[y]
                 print(V_sheild)
                 return V_sheild,Vector_choose
                 break
    Vector_resource,Vector_choose = choosing (V_weapons, V_Sheilds )
## Vector_resource contains the data of what vector choose
##Vector_choose stores either weapon or sheild





class rounds(GRU,VECTOR):
## class rounds calls gru class and vector class to start the race between them
## method defeat1 defeat2 and defeat3 calculate the loss in energy of both vector and gru and also the health of both of them
    def defeat1(x, y):
        x =  GRU.G_ENERGY - GRU.GRU_source[1]
        y = VECTOR.V_HEALTH - (VECTOR.Vector_resource[2] * GRU.GRU_source[2])
        z =  VECTOR.V_ENERGY - VECTOR.Vector_resource[1]
        return x , y , z
    def defeat2(a, b):
        a = GRU.G_ENERGY - GRU. GRU_source[1]
        c = VECTOR.V_ENERGY - VECTOR.Vector_resource[1]
        b =  GRU.G_HEALTH -( GRU. GRU_source[2]* VECTOR.Vector_resource[2])
        return a , b , c
    def defeat3 (q,w):
        q = GRU.G_ENERGY - GRU. GRU_source[1]
        w =  VECTOR.V_ENERGY - VECTOR.Vector_resource[1]
        return q,w

    w=1
    while w:
        ## while loop is used so that rounds between gru and vector continue untill one of them has zero health
        if VECTOR.V_HEALTH == 0 & GRU.G_HEALTH == 0 :
            if VECTOR.V_HEALTH == 0:
                print('end of battle')
                print('Vector Wins')
                w=0
            
            else:
               print('end of battle')
               print('GRU wins')
               w=0

        else:

            ## if conditions is used to see if both chosed weapons or one of them chose sheild or the other chosed sheild
            if GRU.GRU_choose == 'weapon' :

                if VECTOR.Vector_choose == 'sheild':
                    GRU.G_ENERGY,VECTOR.V_HEALTH,VECTOR.V_ENERGY =  defeat1(GRU.GRU_source, VECTOR.Vector_resource)

                    print('GRU ENERGY',GRU.G_ENERGY) 
                    print('GRU HEALTH',GRU.G_HEALTH)
                    print('VECTOR HEALTH',VECTOR.V_HEALTH)
                    print('VECTOR ENERGY',VECTOR.V_ENERGY)
                    
            if GRU.GRU_choose == 'sheild':
                 
                 if VECTOR.Vector_choose == 'weapon':
                     GRU.G_ENERGY,GRU.G_HEALTH,VECTOR.V_ENERGY =  defeat2(GRU.GRU_source, VECTOR.Vector_resource)
                     print('GRU ENERGY',GRU.G_ENERGY) 
                     print('GRU HEALTH',GRU.G_HEALTH)
                     print('VECTOR HEALTH',VECTOR.V_HEALTH)
                     print('VECTOR ENERGY',VECTOR.V_ENERGY)
                     
                     
                     
            if GRU.GRU_choose == 'weapon' :
                     
                     if VECTOR.Vector_choose == 'weapon':
                         GRU.G_ENERGY , VECTOR.V_ENERGY = defeat3(GRU.GRU_source, VECTOR.Vector_resource)
                         print('GRU ENERGY',GRU.G_ENERGY) 
                         print('GRU HEALTH',GRU.G_HEALTH)
                         print('VECTOR HEALTH',VECTOR.V_HEALTH)
                         print('VECTOR ENERGY',VECTOR.V_ENERGY)
                       
        ## calling the two methods             
        GRU_source,GRU_choose = GRU.GRU_choosing(GRU.G_weapons, GRU.G_Sheilds )
        Vector_resource,Vector_choose = VECTOR.choosing (VECTOR.V_weapons,VECTOR.V_Sheilds )
  
