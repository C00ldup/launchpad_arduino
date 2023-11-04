#!/usr/bin/env python
import sys
import arduino

try:
    import launchpad_py as launchpad
except ImportError:
    sys.exit("error loading launchpad_py")

def main():
    forceRotation = 32
    multiplier = False
    
    lp = launchpad.Launchpad()
    lp.Open()
    lp.Reset()

    buttons = {'0':'rotation_sub',
               '2':'rotation_add',
               '1':'multiplier',
               '16':'rotation_left',
               '18':'rotation_right',
               '6':'arm_up',
               '21':'arm_left',
               '23':'arm_right',
               '38':'arm_down',}
    
    forces = {'32':'2',
              '33':'3',
              '34':'4',
              '35':'5',
              '48':'6',
              '49':'7',
              '50':'8',
              '51':'9'}

    lp.LedCtrlRaw( forceRotation, 3, 3 )
    lp.LedCtrlRaw( 72, 3, 2 )
    for key,value in buttons.items():
        if int(key) in {0,1,2}:
            lp.LedCtrlRaw( int(key), 0, 3 )
        else:
            lp.LedCtrlRaw( int(key), 3, 0 )

    while 1:
        but = lp.ButtonStateRaw()
        
        if but != [] and but[1]:
            if str(but[0]) in buttons:
                if(buttons[str(but[0])] == 'multiplier'):
                    if multiplier:
                        multiplier = False
                        lp.LedCtrlRaw( 17, 0, 0 )
                    else:
                        multiplier = True
                        lp.LedCtrlRaw( 17, 1, 1 )
                if(buttons[str(but[0])] == 'rotation_add'):
                    if(forceRotation<51):
                        if forceRotation==35:
                            forceRotation=47
                        forceRotation+=1
                        lp.LedCtrlRaw(forceRotation, 3, 3)
                if(buttons[str(but[0])] == 'rotation_sub'):
                    if(forceRotation>32):
                        lp.LedCtrlRaw(forceRotation, 0, 0)
                        if forceRotation!=51:
                            if forceRotation==48:
                                forceRotation=36
                        forceRotation-=1
                
                
                if(buttons[str(but[0])] == 'rotation_left'):
                    arduino.left(int(forces[str(forceRotation)])*20 if multiplier else int(forces[str(forceRotation)]))
                if(buttons[str(but[0])] == 'rotation_right'):
                    arduino.right(int(forces[str(forceRotation)])*20 if multiplier else int(forces[str(forceRotation)]))

            if but[0] == 72:
                arduino.breakArm()
                break

            #print(arduino.currentAngle)
            #print(forceRotation)
            #print(but[0])

    lp.Reset()
    lp.Close()

    
if __name__ == "__main__":
    main()
