#String is a sequence of characters  enclosed within single,double,triple quotes

name='Sita'
father="sita's father is Janak"
place='''Sita is believed to be found, not biologically born.

King Janaka discovered her while ploughing the field during a yajna.

She emerged from the earth (Bhumi Devi).

Because she came from a furrow (sita means furrow in Sanskrit), she was named Sita.

She was raised as the daughter of King Janaka of Mithila.'''

about=print(f"{name},wife of ram.{father},{place} " )



print(len(place)) #returnn length of string
print(name[0:3]) #used  to acess the  string
print(name[::-1])
print(name[::2])