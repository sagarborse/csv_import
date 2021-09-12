import logging
import pandas as pd
from .models import CsvFile, Image, Client
from config.constants import Constants
from .serializers import ImageSerializer
from datetime import datetime

logger = logging.getLogger(__name__)

class ImportCsv(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.chunksize = Constants.CHUNK_SIZE  # 10 ** 2

    def import_csv_to_db(self):
        logger.info('Import CSV task started')
        try:
            csvs = CsvFile.objects.filter(activate=True)
            csvs = csvs.values()
            for csv in csvs:
                images_list = []
                client = Client.objects.get(id=csv['client_id'])
                # k = Image(image='dsvsvd', title='sdvsd', description='sdvsd', client=client)
                # Image.objects.bulk_create([k], ignore_conflicts=True)
                if client:
                    Image.objects.filter(client=client).delete()
                with pd.read_csv(csv['url'], chunksize=self.chunksize) as reader:
                    for chunk in reader:
                        images = chunk.to_dict('record')
                        for image in images:
                            serializer = ImageSerializer(data={'image': image['image'], 'title': image['title'],
                                                               'description': image['description'],
                                                               'client': csv['client_id']})
                            if serializer.is_valid():
                                now = datetime.now()
                                images_list.append(Image(image=image['image'], title=image['title'], created=now,
                                                         description=image['description'], client=client))
                            else:
                                print(serializer.errors)
                                self.logger.info(serializer.errors)

                        if len(images_list) > 5000:
                            Image.objects.bulk_create(images_list, ignore_conflicts=True)
                            images_list = []
                if images_list:
                    Image.objects.bulk_create(images_list)
        except Exception as exc:
            logger.exception('Celery task failure!!!', exc_info=exc)


