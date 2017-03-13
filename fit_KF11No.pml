set_color br11= [0.647 , 0.000 , 0.149]
set_color br10= [0.843 , 0.188 , 0.153]
set_color br9 = [0.957 , 0.427 , 0.263]
set_color br8 = [0.992 , 0.682 , 0.380]
set_color br7 = [0.996 , 0.878 , 0.565]
set_color br6 = [1.000 , 1.000 , 0.749]
set_color br5 = [0.878 , 0.953 , 0.973]
set_color br4 = [0.671 , 0.851 , 0.914]
set_color br3 = [0.455 , 0.678 , 0.820]
set_color br2 = [0.271 , 0.459 , 0.706]
set_color br1 = [0.192 , 0.212 , 0.584]
load ../analysis2/Nef_Swiss.pdb, 4EN2
create B, resi 83-206
create N, resi 1-82
bg_color white
hide everything
show surface, B
color grey, B
show sphere, N
select P58, object N and resi 58
select P30, object N and resi 30
select P42, object N and resi 42
select P29, object N and resi 29
select P60, object N and resi 60
select P61, object N and resi 61
select P62, object N and resi 62
select P63, object N and resi 63
select P64, object N and resi 64
select P65, object N and resi 65
select P66, object N and resi 66
select P67, object N and resi 67
select P68, object N and resi 68
select P69, object N and resi 69
select P80, object N and resi 80
select P81, object N and resi 81
select P53, object N and resi 53
select P24, object N and resi 24
select P25, object N and resi 25
select P26, object N and resi 26
select P27, object N and resi 27
select P20, object N and resi 20
select P21, object N and resi 21
select P48, object N and resi 48
select P23, object N and resi 23
select P46, object N and resi 46
select P47, object N and resi 47
select P44, object N and resi 44
select P45, object N and resi 45
select P28, object N and resi 28
select P43, object N and resi 43
select P40, object N and resi 40
select P41, object N and resi 41
select P1, object N and resi 1
select P82, object N and resi 82
select P3, object N and resi 3
select P2, object N and resi 2
select P5, object N and resi 5
select P4, object N and resi 4
select P7, object N and resi 7
select P6, object N and resi 6
select P9, object N and resi 9
select P8, object N and resi 8
select P32, object N and resi 32
select P51, object N and resi 51
select P49, object N and resi 49
select P13, object N and resi 13
select P34, object N and resi 34
select P77, object N and resi 77
select P76, object N and resi 76
select P75, object N and resi 75
select P12, object N and resi 12
select P73, object N and resi 73
select P72, object N and resi 72
select P71, object N and resi 71
select P70, object N and resi 70
select P15, object N and resi 15
select P79, object N and resi 79
select P78, object N and resi 78
select P11, object N and resi 11
select P10, object N and resi 10
select P39, object N and resi 39
select P38, object N and resi 38
select P59, object N and resi 59
select P22, object N and resi 22
select P14, object N and resi 14
select P16, object N and resi 16
select P19, object N and resi 19
select P54, object N and resi 54
select P31, object N and resi 31
select P56, object N and resi 56
select P37, object N and resi 37
select P36, object N and resi 36
select P35, object N and resi 35
select P52, object N and resi 52
select P33, object N and resi 33
select P55, object N and resi 55
select P74, object N and resi 74
select P18, object N and resi 18
select P17, object N and resi 17
select P57, object N and resi 57
select P50, object N and resi 50
color br4, P58
color br5, P30
color br6, P42
color br7, P29
color br6, P60
color br5, P61
color br5, P62
color br7, P63
color br5, P64
color br7, P65
color br6, P66
color br5, P67
color br6, P68
color br6, P69
color br5, P80
color br5, P81
color br6, P53
color br6, P24
color br6, P25
color br6, P26
color br6, P27
color br7, P20
color br6, P21
color br6, P48
color br7, P23
color br5, P46
color br5, P47
color br4, P44
color br5, P45
color br7, P28
color br4, P43
color br6, P40
color br4, P41
color br8, P1
color br5, P82
color br6, P3
color br7, P2
color br4, P5
color br6, P4
color br6, P7
color br11, P6
color br9, P9
color br9, P8
color br5, P32
color br4, P51
color br3, P49
color br6, P13
color br3, P34
color br7, P77
color br4, P76
color br5, P75
color br8, P12
color br6, P73
color br5, P72
color br4, P71
color br7, P70
color br7, P15
color br7, P79
color br4, P78
color br4, P11
color br10, P10
color br4, P39
color br4, P38
color br7, P59
color br7, P22
color br6, P14
color br7, P16
color br6, P19
color br4, P54
color br5, P31
color br6, P56
color br4, P37
color br7, P36
color br9, P35
color br4, P52
color br7, P33
color br5, P55
color br7, P74
color br7, P18
color br7, P17
color br4, P57
color br5, P50
zoom complete=1
png ../figures/KF11No_fit.png
