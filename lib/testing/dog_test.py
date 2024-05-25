#!/usr/bin/env python3

from dog import dog

class TestDog:
    '''Dog in dog.py'''

    def test_is_class(self):
        '''is a class with the name "Dog"'''
        fido = dog("Fido")
        assert(type(fido) == dog)

class TestInit:
    '''Dog.__init__ in dog.py'''

    def test_saves_self_name(self):
        '''takes a name as an argument and saves it to self.name'''
        fido = dog("Fido")
        assert(fido.name == "Fido")

    def test_saves_self_breed(self):
        '''takes a breed as an argument and saves it to self.breed'''
        fido = dog("Fido", "Dalmatian")
        assert(fido.breed == "Dalmatian")

    def test_default_breed(self):
        '''sets self.breed = "Mutt" when no breed specified'''
        fido = dog("Fido")
        assert(fido.breed == "Mutt")
