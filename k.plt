set title "Experiment" font ",20"
set datafile separator ","
set term png size 1000,800

set logscale y
set grid

set xlabel "Epoch"
set ylabel "MSE"

set output "neural.png"
plot "avg.csv" u 1:2 with linespoints title "MSE", \
"avg.csv" u 1:3 with points title "dev(MSE)"
