for i in *.wav
do
	sox "$i" -r 16000 -c 1 -b 16 "$i" 1> sox.log 2> sox.err
done