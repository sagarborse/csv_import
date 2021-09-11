import logging
import pandas as pd
from .models import CsvFile, Image, Client
from config.constants import Constants
from .serializers import ImageSerializer


class ImportCsv(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.chunksize = Constants.CHUNK_SIZE  # 10 ** 2

    def import_csv_to_db(self):
        # try:
        csvs = CsvFile.objects.filter(activate=True)
        csvs = csvs.values()
        for csv in csvs:
            images_list = []
            with pd.read_csv(csv['url'], chunksize=self.chunksize) as reader:
                for chunk in reader:
                    images = chunk.to_dict('record')
                    for image in images:
                        serializer = ImageSerializer(data={'image' : image['image'], 'title' : image['title'],
                                                    'description' : image['description'], 'client': csv['id']})
                        if serializer.is_valid():
                            client = Client.objects.get(id=csv['client_id'])
                            images_list.append(Image(image=image['image'], title=image['title'],
                                                    description=image['description'], client=client))
                        else:
                            print(serializer.errors)
                            self.logger.info(serializer.errors)

                    if len(images_list) > 5000:
                        Image.objects.bulk_create(images_list)
                        images_list = []
            if images_list:
                Image.objects.bulk_create(images_list)
