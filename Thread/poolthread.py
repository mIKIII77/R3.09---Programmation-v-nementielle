import time
import concurrent.futures
import requests

imgs_urls = [
        'https://cdn.pixabay.com/photo/2016/05/12/23/03/lamb-1388937_1280.png',
        'https://cdn.pixabay.com/photo/2013/07/13/11/43/tux-158547_1280.png'
]



def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[9]
    img_name = f'{img_name}'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor: # Create a thread pool
    executor.map(download_image, imgs_urls) # map the function to the list of urls

end = time.perf_counter()

print(f'Finished in {round(end-start, 2)} second(s)')