load 4en2.pdb, 4EN2
select M20, chain C and resi 20
create D, chain D
create M, chain M
create C, chain C
bg_color white
hide everything
show surface, M
color green, M
show cartoon, C
color yellow, C
show surface, D
color magenta, D
show sphere, M20
color orange, M20
#set transparency, 0.5
rotate x, -90
rotate y, -90
png M20.png
