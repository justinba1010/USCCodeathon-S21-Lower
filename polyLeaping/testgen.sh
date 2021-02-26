

[[ -e input/ ]] && rm -r input/ 
[[ -e output/ ]] && rm -r output/ 
# rm -r -p output/
mkdir -p input
mkdir -p output



[[ -e samples/input ]] && cp -r samples/input ./
[[ -e samples/output ]] && cp -r samples/output ./



for i in {2..30}
do
  # echo "$(cd "$(dirname "$0")" && pwd -P)"
  echo $i | python3 mkin.py > input/input$i.txt
  python3 ./solutions/sol.py < input/input$i.txt > output/output$i.txt

  echo $i
done


rm -rf cases.zip
zip -r cases input output
