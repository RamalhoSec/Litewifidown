import os
import sys


logo = ("""
   ____________
  |____________|_
   ||--------|| | @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   ||-__     || | @@ HA ha ha you is a dead AP! @@
   ||   --__ || | @@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@
   ||      --|| |     @@@
   ||        || O\    __                            Lite Wirelles Down ver0.1b
   ||        ||  \\  (..)
   ||        ||   \\_|  |_            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ||        ||    \  \/  )           !!      Created by RamalhoSec Team | 20/11/2018          !!
   ||        ||     :    :|           !!      Donate  btc 3DppKRbA9Um3z4wnmVtkqnETnvwsip7WkC   !!                                       
   ||        ||     :    :|           !!      Contact https://github.com/RamalhoSec            !!
   ||        ||     :====:O           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ||        ||     (    )            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!                
   ||__@@@@__||     | `' |            !!      Normal use: litewifidown.py                      !!          
   || @|AP|@ ||     | || |            !!      Direct use:                                      !! 
   ||O@`=='@O||     | || |            !!             -air      Attack with the aireplay-ng     !! 
   ||_@\/\/@_||     |_||_|            !!             -mdk      Attack with the mdk3            !! 
 ----------------   '_'`_`            !!      Options required:                                !! 
/________________\----------\         !!             -i        Set Interface name (-air)(-mdk) !! 
|   GUILLOTINE   |-----------|        !!             -b        Set target BSSID for (-air)     !! 
|  OF WIRELESS NETWORKS      |        !!             -c        Set channel for monitor (-air)  !!  
|____________________________|        !!             -e        Set target ESSID for (-mdk)     !!   
                                      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
""")

def cls():
   os.system('clear')




def start():
   cls()
   print(logo)
   
   if(sys.argv[1] == "-air"):
      print("aireplay-ng attack")
      
      
   if(sys.argv[1] == "-mdk"):
      print("mdk3 attack")
      
try:
   sys.argv[1]
except Exception:
   print("normal attack")
