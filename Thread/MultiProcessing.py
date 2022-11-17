import time 
import multiprocessing
import requests


img_urls = [
        'https://cdn.pixabay.com/photo/2016/05/12/23/03/lamb-1388937_1280.png',
        'https://cdn.pixabay.com/photo/2013/07/13/11/43/tux-158547_1280.png'
]

def download_image(img_url): # function to download the images
    img_bytes = requests.get(img_url).content 
    img_name = img_url.split('/')[9] # get the image name from the url by splitting the url
    img_name = f'{img_name}' # name of the image
    with open('images/'+img_name, 'wb') as img_file: # write the image to a file in the images folder
        img_file.write(img_bytes) 
        print(f'{img_name} was downloaded...') 


if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=download_image, args=[img_urls[0]])
    p2 = multiprocessing.Process(target=download_image, args=[img_urls[1]]) 
    p1.start() # start the process
    p2.start()
    p1.join()  # wait for the process to finish
    p2.join() 
    end = time.perf_counter()
    print(f'Finished in {round(end-start, 2)} second(s)')