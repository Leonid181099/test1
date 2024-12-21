Перейти в командной строке в директорию, куда был скачан архив, в папку в test1.  
Запустить Docker  
docker image build -t python-imagename .  
docker run -p 5000:5000 -d python-imagename  
В другом окне в командной строке ввести python test.py
