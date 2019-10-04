import sys
import os

def main():
    return

if __name__ == '__main__':
    main()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    sys.path.insert(0, dir_path + '/preprocessing')
    sys.path.insert(0, dir_path + '/posprocessing')
    
    import MakeDir
    print(' ')
    print('MAKE CERTAIN DIRECTORIES ARE PROPERLY LOADED')
    print('*************************')
    print('*************************')
    print('*************************')
    MakeDir.main()
    print('*************************')
    print('*************************')
    print('*************************')
    
    
    import db
    db.main()
    print('*************************')
    print('*************************')
    print('*************************')
    
    
    import cpy 
    print('*************************')
    print('*************************')
    print('*************************')
    cpy.exSave()
        
    import rotate
    print('*************************')
    print('*************************')
    print('*************************')
    rotate.exrot()
    
    import RCZ
    print('*************************')
    print('*************************')
    print('*************************')
    RCZ.exrez()
    
    import sblobdec
    sblobdec.exblob()
    

    import SquareCSV
    SquareCSV.exS()
    
    import clean
    clean.exC()
     
    import drawGrids
    drawGrids.draw_grids()
