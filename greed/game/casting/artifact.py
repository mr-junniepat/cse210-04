from game.casting.actor import Actor

class Artifact(Actor):
    """ An actor of the game. 
    The responsibility of the Artifact is to calculate points earn by any different artifact in the game. 

    Attribute:
        super().__init__() = Attributes from the parent Actor.
        _points(int) = Initial points.
    """

    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__()
        self._points = 0

    def get_points(self):
        """Gets Artifact points

        Return:
            Points: Points according to the artifact.
        """
        if (self.get_text() == '*'):
            self._points += 1
        elif (self.get_text() == 'O'):
            self._points -= 1
        elif (self.get_text() == 'x'):
            self._points -= 2
        else:
            self._points += 2 
        
        return self._points


            