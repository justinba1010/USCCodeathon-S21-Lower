#on windows, first use dos2unix genSamples.sh to get rid of windows characters
# then run this file using Bash 
# (accessed through start menu -> run -> Bash)

#or using cmd use bash testgen.sh

for i in {0..1}
do
  echo $i | python3 ./mkin.py > samples/input/input$i.txt
  python3 solutions/sol.py < samples/input/input$i.txt > samples/output/output$i.txt
done
