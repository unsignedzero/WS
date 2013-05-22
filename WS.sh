#Executes WS. Remember to RENAME the file to _ws.py!
# David Tran (unsignedzero)
echo -e "Starting WS.py!"
temp=`python -c "from sys import version_info as v; print(v[0])"`
if [ $temp -eq 2 ]; then
  echo -e "Python 2.X detected\n"
  python WSv2.5.py $@
else if [ $temp -eq 3 ];then
  echo -e "Python 3.X detected\n"
  python WSv3.py $@
else
  echo -e "Unknown python version detected."
fi
fi
