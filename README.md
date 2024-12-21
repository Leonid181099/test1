Перейти в командной строке в директорию, куда был скачан архив, в папку в test1.  
Запустить Docker  
docker image build -t python-imagename .  
docker run -p 5000:5000 -d python-imagename  
В другом окне в командной строке ввести python test.py
и ввести запрос. Также можно ввести test для запроса 'field_name_1=abc@mail.lol&field_name_2=+7 999 999 99 99&field_name_3=+7 999 999 99 99'.
