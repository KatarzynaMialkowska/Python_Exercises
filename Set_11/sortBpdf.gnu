set term pdf enhanced
set output "sortB.pdf"

set title "Sortowanie X"
set xlabel "numer pozycji"              # opis osi x
set ylabel "liczba na pozycji"          # opis osi y
unset key                               # bez legendy

plot "notSort.dat" using 1:2 with points pt 5
plot "sort.dat" using 1:2 with points pt 5