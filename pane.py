class Pane:
    
    # 2d list of empty pane that puzzle pieces go into
    _pane = []
    
    def __init__(self, pane):
        self._pane = pane
    
    def get_pane(self):
        return self._pane