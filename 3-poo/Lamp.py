class Lamp:
    # Global Variables or Constants
    _LAMP = [
         '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''',
        '''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    '''
    ]

    def __init__(self, isTurnOn):
        self._isTurnOn = isTurnOn
    
    def turnOn(self):
        self._isTurnOn = True
        self._displayImages()


    def turnOff(self):
        self._isTurnOn = False
        self._displayImages()

    def _displayImages(self):
        if self._isTurnOn:
            print(self._LAMP[1] + '\n')
        else:
            print(self._LAMP[0]+ '\n')