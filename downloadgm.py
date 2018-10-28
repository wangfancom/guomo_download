
import wget, tarfile
import os

page_num = 98 * 2
for i in range(1, page_num + 1):
  s = str(i) 
  main_path = 'http://p.9grenti.org/uploadfile/2018/0926/07/'
  if i < 10:
    s = s.zfill(2)
  if not os.path.exists(s.zfill(2) + '.jpg'):
    img = main_path + s.zfill(2) + '.jpg'
    print 'download ' + img 
    wget.download(img)

# img='http://p.9grenti.org/uploadfile/2018/0926/07/01.jpg'

# wget.download(img)
