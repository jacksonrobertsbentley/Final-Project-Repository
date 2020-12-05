set terminal windows enhanced  size 600, 500

if(GPVAL_VERSION >= 5.0){set for [i=1:8] linetype i dashtype i}
set size 1.0, 1.0
set origin 0.0, 0.0
set obj 1 rectangle behind from screen 0.0,0.0 to screen 1.0,1.0
set style rectangle fillcolor rgb '#ffffff' fs solid 1.0 noborder
set format '%h'
set xrange [-5.0:5.0]
set yrange [-5.0:5.0]
set zrange [-1.5:1.5]
set cbrange [*:*]
set title ''
set xlabel 'X'
set ylabel 'Y'
set zlabel 'Z'
set datafile missing 'NIL'
unset logscale x
unset logscale y
unset logscale z
set key top center
unset logscale cb
unset grid
unset xzeroaxis
unset yzeroaxis
unset zzeroaxis
set xtics norotate border autofreq
set ytics norotate border autofreq
set ztics norotate border autofreq
set cbtics autofreq
set view 60, 30, 1, 1

set pm3d at s depthorder explicit
set colorbox
set cblabel ''
set palette rgbformulae 7,5,15
splot 'C:/Users/roberts_jack/data11588.gnuplot' index 0 t '' w pm3d lw 1 lt 1 lc rgb '#0000ff'
