'''
util function : copy all images in each folder in a new folder "all-images"
'''
import os
import shutil
try :
    os.makedirs('../data/all-images')
except :
    print("Directory already exists")
classes = os.listdir('../data/dataset/')
print(os.path.join('../data/dataset'))
for cl in classes :
    images=os.listdir('../data/dataset/'+cl)
    for image in images:
        shutil.copy('../data/dataset/' + cl + '/' + image, '../data/all-images/'+cl+'_'+image)
print("Data copied")
