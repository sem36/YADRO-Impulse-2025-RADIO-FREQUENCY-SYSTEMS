# 1.1
`echo "Hello, DevOps!" | tee ~/hello.txt; cat ~/hello.txt`

---
Выводом будет 

Hello, DevOps! -> вывод от tee

Hello, DevOps! -> вывод содержимого файла hello.txt

---
# 1.2
`grep -i "error" /var/log/lastlog | head -n 5`

простой grep запрос /var/log/lastlog, может заменяется на любой другой лог или файл
