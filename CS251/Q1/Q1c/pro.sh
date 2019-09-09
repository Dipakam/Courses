ps -ef | grep -G "^root" | tr -s " "|cut -d " " -f2 > pid.txt

ps -ef | grep -G "^root" | cut -d ":" -f4|cut -d " " -f2- > command.txt
cat pid.txt | awk '{print NR,$0}' > pid1.txt
cat command.txt | awk '{print NR,$0}'>command1.txt
join pid1.txt command1.txt > output.txt


